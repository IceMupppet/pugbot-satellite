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

#form = cgi.FieldStorage()
#try:
#  maximum = int(form.getvalue("history"))
#except:
#  maximum = 1

try:
  with open(config.message_db, 'rb') as f:
    entries = list(csv.reader(f))

    for e in entries:
      if len(e) == 3:
        text = e[2];
        if text.startswith('"') and text.endswith('"'):
          text = text[1:-1]

        result.append({
          'time': e[0],
          'type': e[1],
          'text': text
        })
finally:
  print json.dumps(result, sort_keys=True, indent=4)
    
