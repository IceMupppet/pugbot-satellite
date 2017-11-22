#!/usr/bin/env python

# tests receive.py "web service" for RockBlock

import requests

url = 'http://nogales/rock/receive.py'

message = {
  'imei': '300234010753370',
  'momsn': '12345',
  'transmit_time': '12-10-10 10:41:50',
  'iridium_latitude': '52.3867',
  'iridium_longitude': '0.2938',
  'iridium_cep': '8',
  'data': '48656c6c6f20576f726c6420526f636b424c4f434b'
}

# POST with form-encoded data
r = requests.post(url, data=message)

# Response, status etc
print r.text, r.status_code
