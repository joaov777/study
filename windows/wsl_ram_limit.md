## Limiting the memory usage by WSL 2 on Windows

### 1. Create the file either from Powershell or WSL directly
#### Windows powershell
```bash
notepad.exe C:\Users\YourUsername\.wslconfig
```
#### WSL
```bash
editor "$(wslpath "C:\Users\YourUsername\.wslconfig")"
```

### 2. Add the folowing content to the file
```bash
# Settings apply across all Linux distros running on WSL 2
[wsl2]

# Limits VM memory to use no more than 4 GB, this can be set as whole numbers using GB or MB
memory=4GB 

# Sets the VM to use two virtual processors
processors=2
```
