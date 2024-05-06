$pythonScript = Join-Path -Path $PSScriptRoot -ChildPath "main.py"
Start-Process -FilePath "python" -ArgumentList $pythonScript -WindowStyle Hidden