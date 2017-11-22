#!/bin/sh

v4l2-ctl --list-formats
v4l2-ctl --list-formats-ext
v4l2-ctl --list-devices
v4l2-ctl --get-priority
v4l2-ctl -D
v4l2-ctl -L
v4l2-ctl --all
