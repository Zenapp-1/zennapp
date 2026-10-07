$txtPath = "c:\Zepetto\web adli\ac.txt"
$jsonPath = "c:\Zepetto\web adli\data\akademi-crypto.json"
$imgDir = "c:\Zepetto\web adli\image\AC BACKGROUND"

$content = [IO.File]::ReadAllText($txtPath)
$blocks = [regex]::Split($content, "(?:\r?\n){2,}")

$images = Get-ChildItem -Path $imgDir -File
$imgDict = @{}
foreach ($img in $images) {
    # Normalize name for better matching
    $normalized = $img.BaseName.ToLower().Trim()
    $imgDict[$normalized] = "image/AC BACKGROUND/" + $img.Name
}

$modules = @()
$moduleId = 1

foreach ($block in $blocks) {
    $linesStr = $block.Trim()
    if ([string]::IsNullOrWhiteSpace($linesStr)) { continue }
    
    $lines = [regex]::Split($linesStr, "\r?\n")
    $validLines = @()
    foreach ($L in $lines) {
        $lt = $L.Trim()
        if ([string]::IsNullOrWhiteSpace($lt) -eq $false) {
            $validLines += $lt
        }
    }
    
    if ($validLines.Count -eq 0) { continue }
    
    $title = $validLines[0]
    $materials = @()
    
    for ($i = 1; $i -lt $validLines.Count; $i++) {
        $line = $validLines[$i]
        $httpIdx = $line.IndexOf("http")
        if ($httpIdx -ge 0) {
            $nameStr = $line.Substring(0, $httpIdx).Trim()
            if ($nameStr.EndsWith(":")) {
                $nameStr = $nameStr.Substring(0, $nameStr.Length - 1).Trim()
            }
            $urlStr = $line.Substring($httpIdx).Trim()
            $materials += @{
                name = $nameStr
                url = $urlStr
                image = ""
            }
        } else {
            $materials += @{
                name = $line
                url = ""
                image = ""
            }
        }
    }
    
    $titleKey = $title.ToLower().Trim()
    $imgPath = $null
    
    # Precise Match
    if ($imgDict.ContainsKey($titleKey)) {
        $imgPath = $imgDict[$titleKey]
    }
    
    # Fuzzy Match
    if ($null -eq $imgPath) {
        # remove colons, dashes
        $sanitizedTitle = $titleKey -replace '[:\-\&\s]', ''
        foreach ($key in $imgDict.Keys) {
            $sanitizedKey = $key -replace '[:\-\&\s]', ''
            if ($sanitizedKey -eq $sanitizedTitle -or $sanitizedKey.Contains($sanitizedTitle) -or $sanitizedTitle.Contains($sanitizedKey)) {
                $imgPath = $imgDict[$key]
                break
            }
        }
    }
    
    if ($null -eq $imgPath) {
        $imgPath = "image/crypto.jpeg"
    }
    
    $mod = [ordered]@{
        id = $moduleId
        title = $title
        category = "Crypto"
        level = 1
        description = "Materi pembelajaran tentang $title."
        materials = $materials
        thumbnail = $imgPath
        banner_image = $imgPath
        youtube_url = "https://www.youtube.com"
        pdf_url = ""
    }
    
    $modules += $mod
    $moduleId++
}

$finalData = [ordered]@{
    pageTitle = "Akademi Crypto"
    pageDescription = "Materi belajar Akademi Crypto"
    modules = $modules
}

$json = $finalData | ConvertTo-Json -Depth 10

[IO.File]::WriteAllText($jsonPath, $json, [System.Text.Encoding]::UTF8)

Write-Host "Successfully processed $($modules.Count) modules. Output to $jsonPath"
