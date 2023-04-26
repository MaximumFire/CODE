#! /bin/bash
# Arch Linux install script for lwfinger/rtl8852au wifi driver
# Works for my rtl8832au realtek wifi 6 usb nic

echo "Installing dependencies..."

# install dependencies
sudo pacman -S dkms git make gcc base-devel linux-headers
git clone https://aur.archlinux.org/rtw89-dkms-git.git
cd rtw89-dkms-git
makepkg -sri
cd /home/connor/

echo "Downloading driver..."

# install driver
git clone https://github.com/lwfinger/rtl8852au.git
cd rtl8852au
# not needed as dkms builds anyway
# make
# sudo make install

echo "Installing driver..."

# add to dkms
sudo dkms add .
sudo dkms build rtl8852au -v 1.15.0.1
sudo dkms install rtl8852au -v 1.15.0.1
# if wanted
modinfo 8852au
sudo modprobe 8852au