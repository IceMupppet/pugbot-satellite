#!/bin/sh

if ping -c 1 google.com 2> /dev/null 1> /dev/null
then
  echo "Online"
else
  echo "Not Online"
fi
