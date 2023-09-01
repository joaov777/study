### Mapping a shared folder 
##### Shared folder located on the main computer and available to the VM

## 1. Enable Guest Additions for the VM
- Insert an optical drive for the VM
	- Machine > Settings > Storage > Controller SATA > Add optical drive > OK
	- On the VM window > Devices > Insert Guest Additions CD image

## 2. Create the target mount folder locally on the VM
```bash
mkdir $HOME/MyDocuments
```

## 3. Map the host folder to the VM target folder 
- On the VM Window > Devices > Shared Folders > Shared Folders settings
- Click on "Adds new shared folder" 
- Insert host folder path
- Local VM folder name (MyDocuments)
- Mount point (created on the previous step: /home/joao/MyDocuments)
- Auto-mount and Make Permament

## 4. Enable the mapping
```bash
#sudo mount -t vboxsf foldername /mnt/shared
sudo mount -t vboxsf MyDocumetns /home/joao/MyDocuments
```
