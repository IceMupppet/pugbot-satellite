#!/usr/bin/env python

import datetime
import cgi
#import cgitb; cgitb.enable()  # for troubleshooting
import config
import json
import requests

print "Content-type: application/json"
print

result = [];

form = cgi.FieldStorage()
message = form.getvalue("message")

if message == None:
  message = "test"
  
# call remote url
payload = { 
  'imei': config.imei,
  'username': config.username,
  'password': config.password,
  'data': message.encode('hex')
}

# POST with form-encoded data
r = requests.post(config.rockblock_url, data=payload)

# Result is in the following plain/text format:
# OK,12345678 <-- messageid
# FAILED,errorcode#,Textual description of failure
# Error Code # / Textual description
# 10 Invalid login credentials
# 11 No RockBLOCK with this IMEI found on your account
# 12 RockBLOCK has no line rental
# 13 Your account has insufficient credit
# 14 Could not decode hex data
# 15 Data too long
# 16 No data
# 99 System error
s = str(r.content).rstrip().split(',')
j = {}
j['status'] = s[0];
if s[0] == "OK":
  j['mtmsn'] = s[1];
else:
  j['errno'] = s[1];
  j['error'] = s[2];
  
result.append(j)

with open(config.log, 'a') as log:
    log.write('%s,%s,%s,"%s",' %
        (datetime.datetime.now(), payload['imei'], payload['username'], message ))
    log.write(r.content)
    log.write('\n')

with open(config.message_db, 'a') as msg:
    msg.write('%s,MT,%s\n' % (datetime.datetime.now(), message))

print json.dumps(result, sort_keys=True, indent=4)

