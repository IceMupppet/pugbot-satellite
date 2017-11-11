#!/bin/sh

last root | awk 'NR==1; END{print}'
