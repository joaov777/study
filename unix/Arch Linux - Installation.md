# Arch Linux installation

In this tutorial, you will learn how to install Arch Linux.

- **Checking whether your system supports UEFI or BIOS**

```bash
ls /sys/firmware/efi/efivars
```
_If nothing shows up. Then your system supports BIOS. But if something is displayed on your shell. Then your systems supports UEFI._

- **[Optional] Enabling SSH access for a remote computer installation:**

```bash
sudo systemctl enable sshd.service --now && passwd 
```

- **Initial configuration**

```bash
# for brazillian abnt2 keyboard layout
loadkeys br-abnt2

#enabling wireless/wifi connectivity (make sure you check your wlan device name)
ip -br a 
iwctl station wlan0 scan
iwctl station wlan0 get-networks
iwctl station wlan0 connect <SSID>

# enabling ethernet 
dhclient

# making sure the system time is right
timedatectl set-ntp true

```

- **Overall for partitioning**

```bash
# check current partition and drive status
fdisk -l
lsblk
lsblk --fs
lsblk --fs --ascii

# start partitioning
fdisk /dev/sdX

# commands for fdisk
# p -- show current partition layout
# o -- new partition table for BIOS
# g -- new partition table for UEFI
# n -- new partition
# t -- set partition type (L to list all)
# a -- activate the bootable flag on the partition

```

- **Partitioning process**

```bash
# BIOS Legacy
fdisk /dev/sdX
p
o
n + Enter + Enter + Enter (entire disk used by one single partition)
t + (L to list all and choose ext4)
a + Enter

w
--------
# UEFI
fdisk /dev/sdX
p
g

-- EFI Partition (/dev/sdX1)
n + Enter + Enter + +512M
t + 1  + Enter

-- System Partition (/dev/sdX2)
n + Enter + Enter + Enter (entire disk space left will be used)
t + (L to list all and choose ext4)

w 
```

- **Formatting partitions**

```bash
# BIOS Legacy
mkfs.ext4 /dev/sda1
--------
# UEFI
mkfs.fat -F32 /dev/sda1
mkfs.ext4 /dev/sda2
```

- **Mounting Partitions**

```bash
# BIOS Legacy
mount /dev/sda1 /mnt
--------
# UEFI
mount /dev/sda2 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
```

- **Configuring disks through fstab**

```bash
genfstab -U -p /mnt >> /mnt/etc/fstab
```

- **Downloading Arch Linux core**

```bash
pacstrap -i /mnt base 
```

- **Entering into the freshly installed system and updating root password**

```bash
arch-chroot /mnt
pacman -S base-devel linux linux-firmware linux-headers vim vi nano openssh --noconfirm --needed
```

- **Enabling SSH**

```bash
systemctl enable sshd --now
```

- **Installing important packages**

```bash
pacman -S archlinux-keyring sudo dosfstools os-prober mtools network-manager-applet networkmanager \
wpa_supplicant wireless_tools netctl pavucontrol dialog sudo pulseaudio git \
pulseaudio-alsa --noconfirm --needed
```

- **Enabling Network Manager**

```bash
systemctl enable NetworkManager --now
```

- **Setting system timezone and bios clock**

```bash
ln -sf /usr/share/zoneinfo/America/Fortaleza /etc/localtime
hwclock --systohc

# testar "timedatectl set-timezone America/Fortaleza" e "systemctl enable systemd-timesyncd"
```

- **Setting up system language and keyboard language**

```bash
echo pt_BR.UTF-8 UTF-8 >> /etc/locale.gen &&
echo LANG=pt_BR.UTF-8 > /etc/locale.conf &&
echo KEYMAP=pt_BR.UTF-8 > /etc/vconsole.conf &&
locale-gen

OR

echo en_US.UTF-8 UTF-8 >> /etc/locale.gen &&
echo LANG=en_US.UTF-8 > /etc/locale.conf &&
echo KEYMAP=en_US.UTF-8 > /etc/vconsole.conf &&
locale-gen

```

- **Setting hostname**

```bash
hostnamectl set-hostname myarchbox && hostnamectl
```

- **Setting root password**

```bash
passwd
```

- **Update hosts file**

```bash
echo "127.0.0.1 localhost" > /etc/hosts && echo "127.0.1.1 $HOSTNAME" >> /etc/hosts
```

- **Adding a new user and setting up its new password**

```bash
useradd -m -s /bin/bash -G wheel joao
passwd joao
```

- **Allowing wheel group users to sudo**

```bash
visudo
%wheel ALL=(ALL) ALL
```

- **Installing GRUB boot manager**
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
# Wifi with iwctl
iwctl

#In case ethernet card does not get IP 
dhcpd <ethernet_interface>
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

git clone https://github.com/joaov777/dotfiles.git $HOME/dotfiles && $HOME/dotfiles/dotfiles.sh

#virtualbox related
pacman -S virtualbox-guest-utils xf86-video-vmware mesa mesa-libgl --noconfirm --needed
sudo systemctl enable vboxservice --now
```

---

## Installing DE

- **GNOME**

```bash
sudo pacman -S gnome gdm --noconfirm

# base gnome packages
sudo pacman -S gnome-terminal nautilus gnome-control-center gnome-tweaks gnome-backgrounds --noconfirm --needed

#Enabling login manager
sudo pacman -S gdm --noconfirm && systemctl enable gdm --now
```

- **i3**

```bash
sudo pacman -S i3 ly --noconfirm --needed && systemctl enable ly.service --now
```

- **Deepin**

```bash
sudo pacman -S deepin deepin-extra light-deepin-greeter --noconfirm --needed
sudo pacman -S lightdm lightdm-gtk-greeter --noconfirm --needed
sudo systemctl enable lightdm.service --now
```

- **XFCE**

```bash
sudo pacman -S xfce4 xfce4-goodies xfce4-terminal --noconfirm --needed
sudo pacman -S lightdm lightdm-gtk-greeter --noconfirm --needed
sudo systemctl enable lightdm --now
```

- **KDE Plasma**

```bash
sudo pacman -S plasma-meta kde-applications --noconfirm --needed

# enabling display manager
sudo pacman -S sddm --noconfirm --needed
sudo systemctl enable sddm --now

# useful KDE apps
sudo pacman -S konsole dolphin kate breeze-gtk breeze-kde4 kde-gtk-config ark kinfocenter kwalletmanager gwenview kipi-plugins digikam \
spectacle okular spreedcrunch redshift kfind ktorrent --noconfirm --needed

#Installing KDE plasma addons
sudo pacman -S kdeplasma-addons

#connection tools
sudo pacman -S networkmanager plasma-nm
sudo systemctl enable NetworkManager --now
reboot

```
