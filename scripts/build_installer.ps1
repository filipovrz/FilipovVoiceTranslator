<#
.SYNOPSIS
  Install build deps, run PyInstaller (onedir), optionally compile Inno Setup installer,
  and optionally Authenticode-sign outputs when a certificate is configured.

  Outputs:
    dist\TextToSpeech\TextToSpeech.exe   - portable folder build
    installer_output\FilipovVoiceTranslatorSetup_<version>.exe - if Inno Setup Compiler (ISCC.exe) is available

  Version: read from root VERSION file and injected into installer\TextToSpeech.iss

  Optional signing (reduces SmartScreen warnings when you have a valid code-signing cert):
    $env:TTS_SIGN_CERT = path to .pfx
    $env:TTS_SIGN_PASSWORD = pfx password (optional)
    $env:TTS_SIGN_TIMESTAMP = timestamp URL (default DigiCert)
    Or create code_signing.local.ps1 in the repo root (gitignored).

  Prerequisites: Python venv at ..\.venv with requirements-build.txt installed.
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
Set-Content -Path $issPath -Value $issText -Encoding UTF8 -NoNewline
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
        Write-Warning "signtool.exe not found — skipping signing for $PathToSign"
        return $false
    }
    $ts = if ($env:TTS_SIGN_TIMESTAMP) { $env:TTS_SIGN_TIMESTAMP } else { "http://timestamp.digicert.com" }
    Write-Host "Signing $PathToSign ..."
    $args = @(
        "sign", "/fd", "SHA256", "/td", "SHA256", "/tr", $ts,
        "/f", $cert
    )
    if ($env:TTS_SIGN_PASSWORD) {
        $args += @("/p", $env:TTS_SIGN_PASSWORD)
    }
    $args += $PathToSign
    & $signtool @args
    if ($LASTEXITCODE -ne 0) {
        Write-Error "signtool failed for $PathToSign (exit $LASTEXITCODE)"
    }
    return $true
}

Write-Host "Installing build dependencies..."
& .\.venv\Scripts\pip.exe install -r requirements-build.txt -q

Write-Host "Running PyInstaller..."
& .\.venv\Scripts\pyinstaller.exe --noconfirm --clean TextToSpeech.spec

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

if ($iscc) {
    Write-Host "Compiling Inno Setup installer with: $iscc"
    New-Item -ItemType Directory -Force -Path "installer_output" | Out-Null
    & $iscc "$root\installer\TextToSpeech.iss"
    $setup = Get-ChildItem "installer_output\FilipovVoiceTranslatorSetup_$appVersion.exe" -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($setup) {
        $null = Invoke-CodeSign $setup.FullName
    }
    Write-Host "Done. Check folder: installer_output"
} else {
    Write-Host "Inno Setup 6 not found - skipping .exe installer."
    Write-Host "Portable build: dist\TextToSpeech\"
}

if (-not $env:TTS_SIGN_CERT) {
    Write-Host "Note: set TTS_SIGN_CERT to Authenticode-sign binaries (optional)."
}
