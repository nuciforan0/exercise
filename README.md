need to make it covnert the images to JPG automatically 

can use this in powershell in the mean time
git ls-files | Where-Object { $_ -match '\.jpg$' } | ForEach-Object {
    $new = $_ -replace '\.jpg$', '.JPG'
    git mv --force $_ $new
}

https://nuciforan0.github.io/exercise/exerciseProgram.html
