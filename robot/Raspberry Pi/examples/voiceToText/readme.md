# Getting audio to work
The soundblaster card must be the default device
ex:
```cat /proc/asound/cards
  0 [U0x41e0x30d3   ]: USB-Audio - USB Device 0x41e:0x30d3
                       USB Device 0x41e:0x30d3 at usb-musb-hdrc.1.auto-1.4, full speed
  1 [C920           ]: USB-Audio - HD Pro Webcam C920
                       HD Pro Webcam C920 at usb-musb-hdrc.1.auto-1.3, high speed```
                       
The device `0x41e:0x30d3` is the Creative Play! card

In my experiments, setting the /etc/modprobe.d/alsa-base.conf didn't work, but disabling the audio shield did. I did
this by modifying the `/boot/uEnv.txt` so that the line `cape_disable=capemgr.disable_partno=BB-BONELT-HDMI` was
uncommented