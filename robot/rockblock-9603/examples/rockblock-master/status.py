#!/usr/bin/env python

import math
import cgi
#import cgitb; cgitb.enable()  # for troubleshooting
import json
import csv
import config

print "Content-type: application/json"
print

result = [];

form = cgi.FieldStorage()
try:
  maximum = int(form.getvalue("history"))
except:
  maximum = 1

# TODO: revise to use logfile and extended format

try:
  with open(config.db, 'rb') as f:
    entries = list(csv.reader(f))
    # if specified history is > length of records, use length
    maximum = min(maximum, len(entries))
    # calculate how many entries to skip
    skip = len(entries) - maximum
    # print number of entries specified by history param
    for e in entries:
      if len(e) < 8:
        continue
      if skip:
        skip -= 1
        continue
      result.append({
        'time': e[0],
        'momsn': e[1],
        'imei': e[2],
        'lat': e[7],
        'lng': e[8],
        'speed': e[9],
        'course': e[10],
        'text': e[11]
      })
finally:
  print json.dumps(result, sort_keys=True, indent=4)
    
