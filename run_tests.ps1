$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
if (-not (Test-Path ".\.venv\Scripts\pytest.exe")) {
    Write-Host "Installing dev dependencies..."
    .\.venv\Scripts\pip install -r requirements-dev.txt -q
}
Write-Host "Running pytest..."
.\.venv\Scripts\pytest.exe @args
exit $LASTEXITCODE
