#!/usr/bin/env python

# emulates rockblock api so I don't have to burn credits testing...

import cgi
#import cgitb; cgitb.enable()  # for troubleshooting
import config

print "Content-type: plain/text"
print

form = cgi.FieldStorage()

print "OK,12345"    
