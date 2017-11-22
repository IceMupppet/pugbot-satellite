#PugBot Installation and Configuration


## Pre-Installation

The first thing is to get the network interface up, using wlan0.

     scripts/networkInterfaces-Setup.sh

Then we need to configure for the Access point

     vim /etc/network/interfaces

Add the name of the ssid and the password for both wlan0 and wlan1

Restart the network interfaces

     service networking restart
    
## Installation

Run the main install file as root.

    configure/install.sh

## Package Managers: apt-get and npm

    apt-get install -y rake figlet tmux v4l-utils mencoder ffmpeg cowsay gstreamer0.10-alsa nmap lsof git build-essential cmake zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine-dev libeigen3-dev python-dev python-tk python-numpy python3-dev python3-tk python3-numpy ant default-jdk unzip libpng12-0 libpng12-dev libpng++-dev libpng3 libpnglite-dev zlib1g-dbg zlib1g zlib1g-dev pngtools libjasper-dev libjasper-runtime libjasper1 libjpeg8 libjpeg8-dbg libjpeg62 libjpeg62-dev libjpeg-progs libtiff4-devlibtiff4 libtiffxx0c2 libtiff-tools ffmpeg libavcodec-dev libavformat-dev libswscale-dev openexr libopenexr6 libopenexr-dev


    npm install -g mean-cli express-generator grunt-cli microflo noflo


