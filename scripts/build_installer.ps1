<#
.SYNOPSIS
  Install build deps, run PyInstaller (onedir), optionally compile Inno Setup installer,
  and optionally Authenticode-sign outputs when a certificate is configured.

  Outputs:
    dist\TextToSpeech\TextToSpeech.exe
    installer_output\FilipovVoiceTranslatorSetup_<version>.exe
    FilipovVoiceTranslatorSetup_<version>.exe  (copy in project root for easy testing)

  Version: read from root VERSION file and injected into installer\TextToSpeech.iss

  Optional signing:
    $env:TTS_SIGN_CERT = path to .pfx
    $env:TTS_SIGN_PASSWORD = pfx password (optional)
    $env:TTS_SIGN_TIMESTAMP = timestamp URL (default DigiCert)
    Or create code_signing.local.ps1 in the repo root (gitignored).
#>
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$localSign = Join-Path $root "code_signing.local.ps1"
if (Test-Path $localSign) {
    . $localSign
}

$versionFile = Join-Path $root "VERSION"
if (-not (Test-Path $versionFile)) {
    Write-Error "VERSION file missing at $versionFile"
}
$appVersion = (Get-Content $versionFile -Raw).Trim()
if (-not $appVersion) {
    Write-Error "VERSION file is empty"
}
Write-Host "App version: $appVersion"

$issPath = Join-Path $root "installer\TextToSpeech.iss"
$issText = Get-Content $issPath -Raw -Encoding UTF8
if ($issText -notmatch '#define MyAppVersion "') {
    Write-Error "Could not find MyAppVersion define in TextToSpeech.iss"
}
$issText = [regex]::Replace(
    $issText,
    '#define MyAppVersion "[^"]*"',
    "#define MyAppVersion `"$appVersion`""
)
[System.IO.File]::WriteAllText($issPath, $issText, [System.Text.UTF8Encoding]::new($false))
Write-Host "Updated installer version define to $appVersion"

function Find-SignTool {
    $candidates = @(
        "${env:ProgramFiles(x86)}\Windows Kits\10\bin\*\x64\signtool.exe",
        "${env:ProgramFiles}\Windows Kits\10\bin\*\x64\signtool.exe"
    )
    Get-ChildItem -Path $candidates -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending |
        Select-Object -First 1 -ExpandProperty FullName
}

function Invoke-CodeSign([string]$PathToSign) {
    $cert = $env:TTS_SIGN_CERT
    if (-not $cert -or -not (Test-Path $cert)) {
        return $false
    }
    $signtool = Find-SignTool
    if (-not $signtool) {
        Write-Warning "signtool.exe not found - skipping signing for $PathToSign"
        return $false
    }
    $ts = if ($env:TTS_SIGN_TIMESTAMP) { $env:TTS_SIGN_TIMESTAMP } else { "http://timestamp.digicert.com" }
    Write-Host "Signing $PathToSign ..."
    $signArgs = @(
        "sign", "/fd", "SHA256", "/td", "SHA256", "/tr", $ts,
        "/f", $cert
    )
    if ($env:TTS_SIGN_PASSWORD) {
        $signArgs += @("/p", $env:TTS_SIGN_PASSWORD)
    }
    $signArgs += $PathToSign
    & $signtool @signArgs
    if ($LASTEXITCODE -ne 0) {
        Write-Error "signtool failed for $PathToSign (exit $LASTEXITCODE)"
    }
    return $true
}

Write-Host "Installing build dependencies..."
& .\.venv\Scripts\pip.exe install -r requirements-build.txt -q
if ($LASTEXITCODE -ne 0) {
    Write-Error "pip install failed (exit $LASTEXITCODE)"
}

Write-Host "Running PyInstaller..."
& .\.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean TextToSpeech.spec
if ($LASTEXITCODE -ne 0) {
    Write-Error "PyInstaller failed (exit $LASTEXITCODE)"
}

$exePath = "dist\TextToSpeech\TextToSpeech.exe"
if (-not (Test-Path $exePath)) {
    Write-Error "Build failed: $exePath missing."
}

$null = Invoke-CodeSign (Join-Path $root $exePath)

$iscc = @(
    "${env:LOCALAPPDATA}\Programs\Inno Setup 6\ISCC.exe",
    "${env:ProgramFiles(x86)}\Inno Setup 6\ISCC.exe",
    "${env:ProgramFiles}\Inno Setup 6\ISCC.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1

$setupName = "FilipovVoiceTranslatorSetup_$appVersion.exe"

if ($iscc) {
    Write-Host "Compiling Inno Setup installer with: $iscc"
    New-Item -ItemType Directory -Force -Path "installer_output" | Out-Null
    & $iscc "$root\installer\TextToSpeech.iss"
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Inno Setup compile failed (exit $LASTEXITCODE)"
    }
    $setup = Get-ChildItem "installer_output\$setupName" -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($setup) {
        $null = Invoke-CodeSign $setup.FullName
        $rootCopy = Join-Path $root $setupName
        Copy-Item -Force $setup.FullName $rootCopy
        Write-Host "Installer copied to project root: $rootCopy"
    }
    Write-Host "Done. Check folder: installer_output and project root"
} else {
    Write-Host "Inno Setup 6 not found - skipping .exe installer."
    Write-Host "Portable build: dist\TextToSpeech\"
    $portableZip = Join-Path $root "FilipovVoiceTranslator_${appVersion}_portable.zip"
    if (Test-Path $portableZip) { Remove-Item $portableZip -Force }
    Compress-Archive -Path (Join-Path $root "dist\TextToSpeech\*") -DestinationPath $portableZip
    Write-Host "Portable zip created: $portableZip"
}

if (-not $env:TTS_SIGN_CERT) {
    Write-Host "Note: set TTS_SIGN_CERT to Authenticode-sign binaries (optional)."
}
