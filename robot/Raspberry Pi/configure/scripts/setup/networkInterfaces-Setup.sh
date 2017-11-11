#!/bin/sh
echo "Copy necessary items into /etc/network/interfaces\n"

echo "auto wlan0" >> /etc/network/interfaces
echo "allow-hotplug wlan0" >> /etc/network/interfaces
echo "iface wlan0 inet dhcp" >> /etc/network/interfaces
echo "   wpa-ssid \"WIFI NAME\"" >> /etc/network/interfaces
echo "   wpa-psk \"PASSWORD\"" >> /etc/network/intefaces

echo "auto wlan1" >> /etc/network/interfaces
echo "allow-hotplug wlan1" >> /etc/network/interfaces
echo "iface wlan1 inet dhcp" >> /etc/network/interfaces
echo "   wpa-ssid \"WIFI NAME\"" >> /etc/network/interfaces
echo "   wpa-psk \"PASSWORD\"" >> /etc/network/intefaces


