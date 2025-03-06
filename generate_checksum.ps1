# PowerShell script to generate checksums for AudioTrans Pro installer
Write-Host "Generating checksums for AudioTrans Pro installer..." -ForegroundColor Green

$installerPath = ".\installer\AudioTrans_Setup.exe"
if (Test-Path $installerPath) {
    Write-Host "`nCalculating SHA-256 checksum..." -ForegroundColor Yellow
    $hash = Get-FileHash $installerPath -Algorithm SHA256
    
    $output = @"
AudioTrans Pro Installer Verification
===================================

File: AudioTrans_Setup.exe
Size: $((Get-Item $installerPath).length) bytes
Date: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
SHA-256: $($hash.Hash)

To verify the installer, run this PowerShell command:
Get-FileHash "AudioTrans_Setup.exe" -Algorithm SHA256

The hash should match the SHA-256 value shown above.
"@
    
    # Save the checksums to a file
    $output | Out-File -FilePath ".\installer\CHECKSUMS.txt" -Encoding UTF8
    Write-Host "`nChecksums have been saved to installer\CHECKSUMS.txt" -ForegroundColor Green
} else {
    Write-Host "Error: Installer not found at $installerPath" -ForegroundColor Red
}
