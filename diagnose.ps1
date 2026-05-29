# Deep diagnosis: show hex bytes around the first mojibake sequence
$file = "front\responsavel\dashboard_responsavel.html"
$bytes = [System.IO.File]::ReadAllBytes($file)

Write-Host "=== File Stats ==="
Write-Host "Total bytes: $($bytes.Length)"
Write-Host "First 6 bytes (hex): $(($bytes[0..5] | ForEach-Object { $_.ToString('X2') }) -join ' ')"

# Find the byte sequence for the corrupted characters
# Look for 0xC3 0x83 (= "Ã" double-encoded as UTF-8)
Write-Host "`n=== Looking for 0xC3 0x83 (double-encoded 'Ã') ==="
$found = 0
for ($i = 0; $i -lt $bytes.Length - 1; $i++) {
    if ($bytes[$i] -eq 0xC3 -and $bytes[$i+1] -eq 0x83) {
        $ctx = ($bytes[[Math]::Max(0,$i-2)..[Math]::Min($bytes.Length-1,$i+5)] | ForEach-Object { $_.ToString('X2') }) -join ' '
        Write-Host "Found at offset $i : $ctx"
        $found++
        if ($found -ge 5) { Write-Host "... (more)"; break }
    }
}
if ($found -eq 0) { Write-Host "NOT found." }

# Also look for original UTF-8 pattern C3 A1 (á in UTF-8)
Write-Host "`n=== Looking for 0xC3 0xA1 (correct UTF-8 'á') ==="
$found2 = 0
for ($i = 0; $i -lt $bytes.Length - 1; $i++) {
    if ($bytes[$i] -eq 0xC3 -and $bytes[$i+1] -eq 0xA1) {
        $ctx = ($bytes[[Math]::Max(0,$i-2)..[Math]::Min($bytes.Length-1,$i+3)] | ForEach-Object { $_.ToString('X2') }) -join ' '
        Write-Host "Found at offset $i : $ctx"
        $found2++
        if ($found2 -ge 5) { Write-Host "... (more)"; break }
    }
}
if ($found2 -eq 0) { Write-Host "NOT found." }

# Show a 20-byte window around offset 200 (likely to be in text content)
Write-Host "`n=== 20 bytes at offset 100 ==="
$window = ($bytes[100..119] | ForEach-Object { $_.ToString('X2') }) -join ' '
Write-Host $window

$latin1 = [System.Text.Encoding]::GetEncoding(1252)
$utf8 = [System.Text.Encoding]::UTF8

Write-Host "`n=== Bytes at offset 100-119 decoded ==="
Write-Host "Latin-1: $($latin1.GetString($bytes[100..119]))"
Write-Host "UTF-8:   $($utf8.GetString($bytes[100..119]))"
