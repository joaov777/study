sudo pacman -S linux61-virtualbox-host-modules virtualbox-guest-iso virtualbox-guest-utils virtualbox --noconfirm --needed
sudo su
vboxreload
sudo gpasswd -a $USER vboxusers
