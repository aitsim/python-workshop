#!/usr/bin/env python3

import sys
import urllib.request
import xml.etree.ElementTree as XML


# print("hello world")
# for i in range(10):
#     print(i)

if len(sys.argv) != 3:
    raise SystemExit('USE 3 Argements')


route = sys.argv[1]
stopid = sys.argv[2]




u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(stopid,route))
data = u.read()

doc = XML.fromstring(data)
import pdb; pdb.set_trace()
for pt in doc.findall('*/pt'):
    print(pt.txt)
