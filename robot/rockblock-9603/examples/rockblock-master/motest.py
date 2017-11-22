#!/usr/bin/env python

## Emulate Mobile Originated messages (posts to receive.py web service)
##
## usage: motest.py "message"

import sys
import requests
import time
import config

url="http://localhost/rock/receive.py"

momsn = 0

if len(sys.argv) != 2:
	print "usage: %s \"message\"" % (sys.argv[0])
else:
	mydata = sys.argv[1]
	message = {
		'imei': '300234010753370',
		'momsn': momsn,
		'transmit_time': '12-10-10 10:41:50', # TODO: make this the real date/time
		'iridium_latitude': '99.9999',
		'iridium_longitude': '199.9999',
		'iridium_cep': '8',
		'data': mydata.encode('hex')
	}
	momsn += 1
	print message
	# POST with form-encoded data
	r = requests.post(url, data=message)
	# Response, status etc
	print r.text, r.status_code
	time.sleep(20)
