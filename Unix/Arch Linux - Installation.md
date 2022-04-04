# Arch Linux installation

In this tutorial, you will learn how to install Arch Linux.

- **Check whether your system supports UEFI or BIOS**

```bash
ls /sys/firmware/efi/efivars
```

<aside>
💡 **If nothing shows up**. Then your system supports BIOS.
**If something is displayed on your shell**. Then your systems supports UEFI.

</aside>

- **[Optional] Enabling SSH access for a remote computer installation:**

```bash
sudo systemctl start sshd.service
sudo systemctl enable sshd.service --now
passwd 
```

- **Initial configuration**

```bash
loadkeys br-abnt2
ping 8.8.8.8

#Enabling wireless/wifi connectivity
wifi-menu

#Enabling ethernet addressing
dhclient

#Making sure the system time is right
timedatectl set-ntp true

```

- **Partitioning the system**

```bash
fdisk -l
lsblk

#You can use fdisk (cli) or cfdisk (graphical) for partitioning
fdisk /dev/sdX **OR** cfdisk /dev/sdX 

#For this installation
/dev/sda1 --> /boot ==> 512M
/dev/sda2 --> / ==> Left space
```

- **Formatting partitions**

```bash
#BIOS Legacy
mkfs.ext4 /dev/sda1
mkfs.ext4 /dev/sda2
--------
#UEFI
mkfs.fat -F32 /dev/sda1
mkfs.ext4 /dev/sda2
```

- **Mounting Partitions**

```bash
#BIOS Legacy
mount /dev/sda2 /mnt
ls /mnt #(lost+found)

--------

#UEFI
mount /dev/sda2 /mnt
ls /mnt #(lost+found)
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
```

- **Edit resolv.conf**

```bash
echo "options timeout:1" >> /etc/resolv.conf
```

- **Downloading Arch Linux core**

```bash
pacstrap /mnt base linux linux-firmware vim vi nano netctl
```

- **Configuring disks through fstab**

```bash
genfstab -U -p /mnt >> /mnt/etc/fstab
```

- **Entering into the freshly installed system and updating root password**

```bash
arch-chroot /mnt
passwd
```

- **Setting system timezone and bios clock**

```bash
ln -sf /usr/share/zoneinfo/America/Fortaleza /etc/localtime
hwclock --systohc
```

- **Setting up system language and keyboard language**

```bash
echo pt_BR.UTF-8 UTF-8 >> /etc/locale.gen
echo LANG=pt_BR.UTF-8 > /etc/locale.conf
echo KEYMAP=pt_BR.UTF-8 > /etc/vconsole.conf
locale-gen

OR

echo en_US.UTF-8 UTF-8 >> /etc/locale.gen
echo LANG=en_US.UTF-8 > /etc/locale.conf
echo KEYMAP=en_US.UTF-8 > /etc/vconsole.conf
locale-gen

```

- **Setting hostname**

```bash
echo arch > /etc/hostname
cat /etc/hostname
```

- **Update hosts file**

```bash

echo "127.0.0.1 localhost" > /etc/hosts &&
echo "::1 localhost" >> /etc/hosts &&
echo "127.0.0.1 `hostname`.localdomain `hostname`" >> /etc/hosts
```

- **Adding a new user and setting up its new password**

```bash
useradd joao -m -s /bin/bash -G wheel,audio,video,optical,storage
passwd joao
```

- **Installing important packages**

```bash

pacman -S dosfstools os-prober mtools network-manager-applet networkmanager \
wpa_supplicant wireless_tools pavucontrol dialog sudo pulseaudio git \
pulseaudio-alsa --noconfirm --needed
```

- **Allowing wheel group users to sudo**

```bash
visudo
%wheel ALL=(ALL) ALL
```

- **Installing boot manager**
    - BIOS Legacy
    
    ```bash
    pacman -S grub --noconfirm
    grub-install --target=i386-pc --recheck /dev/sda
    grub-mkconfig -o /boot/grub/grub.cfg
    exit
    reboot
    ```
    

- UEFI

```bash
sudo pacman -S grub-efi-x86_64 efibootmgr
grub-install --target=x86_64-efi --efi-directory=/boot/efi \
--bootloader-id=arch_grub --recheck

grub-mkconfig -o /boot/grub/grub.cfg
exit
reboot
```

---

## After Base Arch Linux installation

- **Check internet connectivity**

```bash
ping 8.8.8.8
host uol.com.br
ping google.com

#In case of wifi (download netctl package)
wifi-menu

#might be necessary to enable networkmanager
sudo systemctl enable NetworkManager --now
sudo systemctl status NetworkManager

#In case ethernet card does not get IP 
dhcpd <ethernet_interface>
```

- **[Optional] Installing openssh for remote access**

```bash
sudo pacman -S openssh
sudo systemctl start sshd.service
sudo systemctl enable sshd.service --now
```

- **Syncronizing and updating package database**

```bash
sudo pacman -Syyuu
```

- **Installing Xorg**

```bash
sudo pacman -S xorg xorg-server --noconfirm
```

- **[Optional] Installing personal packages**

```bash
visudo
%wheel ALL=(ALL) NOPASSWD:ALL

git clone https://github.com/joaov777/mainconf.git
~/mainconf/mainconf.sh

visudo
#%wheel ALL=(ALL) NOPASSWD: ALL

#virtualbox related
pacman -S virtualbox-guest-utils virtualbox-guest-modules-arch \
mesa mesa-libgl --noconfirm
```

---

## Installing DE

- **GNOME**

```bash
pacman -S gnome gdm --noconfirm

#Downloading important tools for gnome
pacman -S gnome-terminal nautilus gnome-control-center gnome-tweaks \
gnome-backgrounds

adwaita-icon-theme --noconfirm

#Enabling login manager
pacman -S gdm --noconfirm
systemctl enable gdm --now
```

- **i3**

```bash
pacman -S i3 ly --noconfirm --needed
systemctl enable ly.service --now
```

- **Deepin**

```bash
pacman -S deepin deepin-extra light-deepin-greeter --noconfirm
pacman -S lightdm lightdm-gtk-greeter --noconfirm
systemctl enable lightdm.service --now
```

- **XFCE**

```bash
pacman -S xfce4 xfce4-goodies xfce4-terminal --noconfirm
pacman -S lightdm lightdm-gtk-greeter --noconfirm
systemctl enable lightdm.service --now
```

- **KDE Plasma**

```bash
#maybe is necessary
echo "exec startkde" > ~/.xinitrc

#sudo pacman -S plasma-meta
#sudo pacman -S plasma-desktop
sudo pacman -S plasma

#Enabling display manager
sudo pacman -S sddm
sudo systemctl enable ssdm.service --now

#Useful KDE apps
sudo pacman -S konsole dolphin kate breeze-gtk breeze-kde4 kde-gtk-config
sudo pacman -S ark kinfocenter kwalletmanager gwenview kipi-plugins digikam \
spectacle okular spreedcrunch redshift kfind ktorrent

sudo nano /etc/sddm.conf
[ Theme ] 
Current=breeze

#Installing KDE plasma addons
sudo pacman -S kdeplasma-addons

#connection tools
sudo pacman -S networkmanager plasma-nm
sudo systemctl enable NetworkManager --now
reboot

```