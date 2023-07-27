
### 1. Download rclone
sudo apt install rclone -y

### 2. Create the tunnel from your current machine
```bash
ssh -L localhost:53682:localhost:53682 username@remote_server
```
### 3. Setup rclone in the headless machine
```bash
rclone config 
n
IFCE
13
1 (full access)
not a headless machine (choose Y)
```
### 4. Copy the link provided into the local browser and use port 56382
### 5. Authenticate with the Gmail account chosen
