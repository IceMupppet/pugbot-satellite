#!/bin/sh
echo "Open Ports:" | figlet
netstat -pln | grep tcp | awk '{ print "Port: " $4 " open by " $7 }' 
