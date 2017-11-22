#!/usr/bin/env python

import sys
import os
from rbControl import RockBlockControl

                     
if __name__ == '__main__':
    if len(sys.argv) == 1:
        RockBlockControl("/dev/ttyUSB0").mt_recv()
    else:
        print "usage: %s" % os.path.basename(sys.argv[0])
        exit(1)
        
   
