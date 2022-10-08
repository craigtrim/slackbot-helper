# Full path of the file
$file = 'setup.py'
$ProjectName = "find-reaction"
$ProjectVersion = "0.1.0"

# remove the file if it exists
if (Test-Path -Path $file -PathType Leaf) {
    Remove-Item $file
}

Push-Location dist
tar -xf ".\$ProjectName-$ProjectVersion.tar.gz"
Move-Item ".\$ProjectName-$ProjectVersion\setup.py" ../.
Remove-Item "$ProjectName-$ProjectVersion" -Recurse
Pop-Location
