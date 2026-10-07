$txtFile = "c:\Zepetto\web adli\TU.txt"
$imgDir = "c:\Zepetto\web adli\image\TU BACKGROUND"
$outputFile = "c:\Zepetto\web adli\data\ternak-uang.json"

$lines = Get-Content $txtFile -Encoding UTF8

$modules = @()
$currentModule = $null
$moduleId = 1

# List all images in the directory
$imageFiles = Get-ChildItem -Path $imgDir -File | Select-Object Name, Extension

function Normalize-String($str) {
    if ([string]::IsNullOrWhiteSpace($str)) { return "" }
    $str = $str -replace '[^\w]', ''
    return $str.ToLower()
}

function Find-Image($title) {
    $normTitle = Normalize-String $title
    foreach ($img in $imageFiles) {
        $imgNameNoExt = [System.IO.Path]::GetFileNameWithoutExtension($img.Name)
        $normImg = Normalize-String $imgNameNoExt
        if ($normImg -eq $normTitle) {
            return "image/TU BACKGROUND/" + $img.Name
        }
    }
    return ""
}

foreach ($line in $lines) {
    $trimLine = $line.Trim()

    if ($trimLine -eq "") {
        if ($currentModule -ne $null) {
            $modules += $currentModule
            $currentModule = $null
        }
        continue
    }

    if ($currentModule -eq $null) {
        $imgUrl = Find-Image $trimLine
        
        $currentModule = @{
            id = $moduleId
            title = $trimLine
            category = "Ternak Uang"
            level = 1
            description = "Materi pembelajaran tentang $trimLine."
            materials = @()
            thumbnail = $imgUrl
            banner_image = $imgUrl
            youtube_url = "https://www.youtube.com"
            pdf_url = ""
        }
        $moduleId++
    } else {
        # parse material
        if ($trimLine -match '^(.*?):\s*(https?://[^\s]+)') {
            $nameStr = $matches[1].Trim()
            $urlStr = $matches[2].Trim()

            # Optional: remove " Ternak Uang" from the end of the name if present
            if ($nameStr.EndsWith(" Ternak Uang", [System.StringComparison]::InvariantCultureIgnoreCase)) {
                $nameStr = $nameStr.Substring(0, $nameStr.Length - 12).Trim()
            }

            $material = @{
                url = $urlStr
                name = $nameStr
                image = ""
            }
            $currentModule.materials += $material
        }
    }
}

if ($currentModule -ne $null) {
    $modules += $currentModule
}

$outputData = @{
    modules = $modules
}

$json = $outputData | ConvertTo-Json -Depth 5 -Compress
# Make json beautiful
# Note: PowerShell 5.1 ConvertTo-Json depth 5 without compress is decent, but can be huge if large depth
$jsonUncompressed = $outputData | ConvertTo-Json -Depth 5
Set-Content -Path $outputFile -Value $jsonUncompressed -Encoding UTF8

Write-Host "Done! Generated $modules.Count modules based on TU.txt."
