#!/bin/sh

echo "\n      ___         ___           ___                         ___                   "                   
echo "\n     /\  \       /\  \         /\__\         _____         /\  \                  "  
echo "\n    /::\  \      \:\  \       /:/ _/_       /::\  \       /::\  \         ___     " 
echo "\n   /:/\:\__\      \:\  \     /:/ /\  \     /:/\:\  \     /:/\:\  \       /\__\    "
echo "\n  /:/ /:/  /  ___  \:\  \   /:/ /::\  \   /:/ /::\__\   /:/  \:\  \     /:/  /    "
echo "\n /:/_/:/  /  /\  \  \:\__\ /:/__\/\:\__\ /:/_/:/\:|__| /:/__/ \:\__\   /:/__/     "
echo "\n \:\/:/  /   \:\  \ /:/  / \:\  \ /:/  / \:\/:/ /:/  / \:\  \ /:/  /  /::\  \     "
echo "\n  \::/__/     \:\  /:/  /   \:\  /:/  /   \::/_/:/  /   \:\  /:/  /  /:/\:\  \    " 
echo "\n   \:\  \      \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /   \/__\:\  \   "
echo "\n    \:\__\      \::/  /       \::/  /       \::/  /       \::/  /         \:\__\  "
echo "\n     \/__/       \/__/         \/__/         \/__/         \/__/           \/__/  "
echo "\n "
echo "\n        ROBOT WEBSERVER INSTALLATION SCRIPT:  Raspberry Pi 3+ Ubuntu 16.01+ "                                                                                                         

# Installing external packages using apt-get

echo "\nUpgrade/update package manager, repositories and packages"

echo "\n**************  Package Management:"
apt-get -y update

apt-get -y upgrade

apt-get -y dist-upgrade

echo "\n**************  Display Packages:"

apt-get install -y figlet tmux cowsay 

echo "\n**************  Video Packages:"

apt-get install -y v4l-utils gstreamer0.10-alsa mencoder ffmpeg libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine-dev zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev

echo "\n**************  Audio Packages"

apt-get install -y portaudio19-dev mpg123

echo "\n**************  Network Packages:"

apt-get install -y nmap

echo "\n**************  Bluetooth Packages:"

apt-get install -y pi-bluetooth bluetooth bluez libbluetooth-dev libudev-dev

echo "\n**************  Programming Packages -> Javascript"

apt-get install -y node nodejs default-jdk ant

echo "\n**************  Programming Packages -> Python" 

apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy 

echo "\n**************  Programming Packages -> Robot Operating System (ROS):"

apt-get install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall ros-groovy-sphero-bringup

echo "\n**************  Programming Packages -> Utilities" 

apt-get install -y libeigen3-dev build-essential cmake

echo "\n**************  Utilities:"

apt-get install -y lsof git rake unzip zsh

echo "\n**************  Libraries:"

apt-get install -y libpng12-0 libpng12-dev libpng++-dev libpng3 libpnglite-dev zlib1g-dbg zlib1g zlib1g-dev pngtools libjasper-dev libjasper-runtime libjasper1 

apt-get install -y libjpeg8 libjpeg8-dbg libjpeg62 libjpeg62-dev libjpeg-progs libtiffxx0c2 libtiff-tools ffmpeg libavcodec-dev libavformat-dev 

apt-get install -y libswscale-dev openexr libopenexr6 libopenexr-dev libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev


# Special packages, binaries and wget installs

echo "NGROK" | figlet

echo "Installing ngrok binary and moving it into the /usr/bin"

unzip binaries/ngrok.zip

mv ngrok /usr/bin/

# Installing Golang and moving it into the PATH

echo "GOLANG" | figlet

echo "Installing Golang for ARM and moving it into /usr/local/"

wget https://storage.googleapis.com/golang/go1.8.linux-armv6l.tar.gz

tar -C /usr/local -xzf go1.8.linux-armv6l.tar.gz

echo "Exporting Path information for go"

export PATH=$PATH:/usr/local/go/bin

# MEAN -> Mongo, Express, AngularJS and Node. 

echo "NODE" | figlet

echo "Grab the MEAN command line tool"

npm install -g mean-cli 

echo "Setting up express server"

npm install -g express-generator

echo "Install Cylon.js and Sphero cylon"

npm install -g cylon cylon-sphero cylon-sphero-ble cylon-ble cylon-api-socketio cylon-raspi cylon-audio cylon-firmata cylon-api-http

echo "Install Grunt and Grunt CLI tools"

npm install -g grunt-cli

echo "RUBY" | figlet

echo "Ruby gem file for Sphero and serial port"

gem install sphero

echo "REPOS" | figlet

echo "Installing global .gitignore file"

git config --global core.excludesfile etc/skel/.gitignore

echo "SECURITY" | figlet

echo "-----WIP---- SSHD, FTP, HTTP, USERS, SERVICES"

echo "CLEANUP" | figlet

echo "removing unnecessary packages from apt-get"

# Installing bluetooth tools with BlueZ

echo "BLUEZ" | figlet

echo "Grabbing the working BlueZ Source Code"

wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.37.tar.xz

tar xvf bluez-5.37.tar.xz

cd bluez-5.37

echo "Configuring BlueZ its the classic ./configure & make & make install"

./configure
make
make install

cd ..

echo "Enable Bluetooth Low Energy"

cp -f lib/systemd/system/bluetooth.service /lib/systemd/system/bluetooth.service

echo "Restarting Bluetooth...."

systemctl status bluetooth
systemctl start bluetooth
systemctl enable bluetooth

# Deal with SSH Configuration and Banner

echo "SSH" | figlet

echo "Copying SSH Banner (issue and issue.net)"

cp -f etc/issue /etc/

cp -f etc/issue.net /etc/

# Message of the Day information

echo "MOTD" | figlet

echo "Copying MOTD files into /etc/update.d/"

cp -rf etc/update-motd.d /etc/

echo "Update Hostname file for Pugbot"

cp -f etc/hostname /etc/hostname

# /etc/skel is the default user information.  Let's make sure it's always setup correctly.

echo "USER" | figlet

echo "Copying default User variables into /etc/skel/"

cp -rf etc/skel/ /etc/

echo "Setting up root account"

cp -rf scripts/ /root/
cp -f etc/skel/.vimrc /root/.vimrc
cp -f etc/skel/.bashrc /root/.bashrc
cp -f etc/skel/.tmux.conf /root/.tmux.conf

apt-get -y autoremove

reboot

