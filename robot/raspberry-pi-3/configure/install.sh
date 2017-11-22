#!/bin/sh

# Installing external packages using apt-get

echo "Upgrade/update package manager, repositories and packages"

echo "\n**************  Package Manager:"
apt-get -y update

apt-get -y upgrade

apt-get -y dist-upgrade

echo "\n**************  Display Packages:"
apt-get install -y figlet tmux cowsay 

echo "\n**************  Video Packages:"
apt-get install -y v4l-utils gstreamer0.10-alsa mencoder ffmpeg libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine-dev zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev portaudio19-dev

echo "\n**************  Network Packages:"
apt-get install -y nmap

echo "\n**************  Programming Packages:" 

apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy ant default-jdk libeigen3-dev build-essential cmake

echo "\n**************  Utilities:"
apt-get install -y lsof git rake unzip 

echo "\n**************  Libraries:"
apt-get install -y libpng12-0 libpng12-dev libpng++-dev libpng3 libpnglite-dev zlib1g-dbg zlib1g zlib1g-dev pngtools libjasper-dev libjasper-runtime libjasper1 libjpeg8 libjpeg8-dbg libjpeg62 libjpeg62-dev libjpeg-progs libtiffxx0c2 libtiff-tools ffmpeg libavcodec-dev libavformat-dev libswscale-dev openexr libopenexr6 libopenexr-dev

echo "\n**************  Binaries:"
unzip binaries/ngrok.zip
mv ngrok /usr/bin/



# Deal with SSH Configuration and Banner

echo "SSH" | figlet

echo "Copying SSHD Configuration files into /etc/ssh/"

cp -f etc/ssh/sshd_config /etc/ssh/sshd_config

echo "Copying SSHD Banner Files"

cp -f etc/ssh/sshd-banner /etc/ssh/sshd-banner

# Message of the Day information

echo "MOTD" | figlet

echo "Copying MOTD files into /etc/init.d/"

cp -f etc/init.d/motd /etc/init.d/motd

cp -f etc/hostname /etc/hostname

# /etc/skel is the default user information.  Let's make sure it's always setup correctly.

echo "USER" | figlet

echo "Copying default User variables into /etc/skel/"

cp -rf etc/skel/ /etc/

echo "Setting up root account"

cp -rf scripts/ /root/

cp -f /etc/skel/.vimrc /root/.vimrc
cp -f /etc/skel/.bashrc /root/.bashrc
cp -f /etc/skel/.tmux.conf /root/.tmux.conf

# MEAN -> Mongo, Express, AngularJS and Node. 

echo "SERVER" | figlet

echo "Grab the MEAN command line tool"

npm install -g mean-cli 

echo "Setting up express server"

npm install -g express-generator

echo "Install Cylon.js and Sphero cylon"

npm install -g cylon cylon-sphero

echo "Install Grunt and Grunt CLI tools"

npm install -g grunt-cli

echo "Install noflo node modules"

npm install -g noflo

echo "Install microflo node modules"

npm install -g microflow

echo "APACHE 2" | figlet

echo "Changing Apache2 port from 8080 to 80"

cp -f etc/apache2/ports.conf /etc/apache2/ports.conf

echo "Copying over /var/www/  PUG html website"

cp -rf www/ /var/www/html

echo "DEBLOT" | figlet

echo "Free Port 3000: Disable BeagleBone Cloud9 Services ->  scripts/setup/stop3000.sh"

scripts/setup/stop3000.sh

echo "Free Port 80: Disable Bonescript -> scripts/setup/stop80.sh"

scripts/setup/stop80.sh

echo "Free Port 3350 & 3389: Remove xrdp -> scripts/setup/disable-xrdp.sh"

scripts/setup/disable-xrdp.sh

echo "REPOS" | figlet

echo "Installing global .gitignore file"

git config --global core.excludesfile etc/skel/.gitignore

echo "Ruby gem files for beaglebone black IO control"

gem install beaglebone

echo "Ruby gem file for Sphero and serial port"

gem install sphero

echo "ROS python wrappers for Sphero" 

git clone https://github.com/mmwise/sphero_ros.git scripts/repos/ROS

echo "Python SDK for Sphero"

git clone https://github.com/faulkner/sphero.git scripts/repos/python

echo "Node.JS Sphero SDK"

git clone https://github.com/mick/node-sphero.git scripts/repos/node-sphero

echo "Camera streaming C++ examples"

git clone git clone git://github.com/derekmolloy/boneCV examples/usb-camera-streaming

echo "UART" | figlet

echo "Enabling UART1 in /mnt/boot/uEnv.txt (Requires reboot)"

scripts/setup/enableUART2.sh

echo "Disabling Onboard Audio"
scripts/setup/disable-usb-audio.sh


echo "CLEANUP" | figlet

echo "removing unnecessary packages from apt-get"

apt-get -y autoremove

reboot

