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
echo "\n        HOSTED WEBSERVER INSTALLATION SCRIPT:  Ubuntu 16.01+ Linux Server" 

# Installing external packages using apt-get

echo "\nUpgrade/update package manager, repositories and packages"

echo "\n**************  Package Manager:"
apt-get -y update

apt-get -y upgrade

apt-get -y dist-upgrade

echo "\n**************  Display Packages:"
apt-get install -y figlet tmux cowsay 

echo "\n**************  Network Packages:"
apt-get install -y nmap ca-certificates

echo "\n**************  Programming Packages:" 

apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy ant default-jdk build-essential cmake

echo "\n**************  Utilities:"
apt-get install -y lsof git rake unzip update-motd


echo "\n**************  Binaries:"
unzip binaries/ngrok.zip
mv ngrok /usr/bin/


# Deal with SSH Configuration and Banner

echo "SSH" | figlet

echo "Copying SSHD Configuration files into /etc/ssh/"

cp -f etc/ssh/sshd_config /etc/ssh/sshd_config

# Message of the Day information

echo "MOTD" | figlet

echo "Copying MOTD files into /etc/init.d/"

#cp -f etc/init.d/motd /etc/init.d/motd

echo "Copying Hosname information"
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

echo "Install Grunt and Grunt CLI tools"

npm install -g grunt-cli

echo "REPOS" | figlet

echo "Installing global .gitignore file"

git config --global core.excludesfile etc/skel/.gitignore

echo "CLEANUP" | figlet

echo "removing unnecessary packages from apt-get"

apt-get -y autoremove

reboot