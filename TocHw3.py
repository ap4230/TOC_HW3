# -*- coding: utf-8 -*-

import sys
import urllib2
import json

total = 0
item = 0

district = unicode(sys.argv[2], 'utf-8')
road = unicode(sys.argv[3], 'utf-8')
year = int(sys.argv[4]) * 100

response = urllib2.urlopen(sys.argv[1])
text = json.load(response)

for i in range(len(text)):
    if text[i][u"鄉鎮市區"].find(district) != -1 :
        if text[i][u"土地區段位置或建物區門牌"].find(road) != -1:
            if text[i][u"交易年月"] > year :
                total += text[i][u"總價元"]
                item += 1

avg_price = total / item
print int(avg_price)
