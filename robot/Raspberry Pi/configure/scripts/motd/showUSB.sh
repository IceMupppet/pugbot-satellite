#!/bin/sh

        echo "USB" | figlet 
        lsusb | cut -d: -f3 | awk '{$1 = ""; print $0;}'
