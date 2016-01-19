#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#Chuck Norris 
import urllib
import json

url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'

resp = urllib.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

print (data['value']['joke'])

