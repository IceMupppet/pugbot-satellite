#!/usr/bin/env python

import sys
import os
from rbControl import RockBlockControl
                     
if __name__ == '__main__':
    if len(sys.argv) == 2:
        RockBlockControl("/dev/ttyUSB0").mo_send(sys.argv[1])
    else:
        print "usage: %s message" % os.path.basename(sys.argv[0])
        exit(1)
        
   
