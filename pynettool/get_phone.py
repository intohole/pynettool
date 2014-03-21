#coding=utf-8

from pynet import PyNet
import json
import time


p = PyNet()
for i in range(1):
	data = p.dianxin_phone()
	data = json.loads(data)
	for i  in data:
		phone =  str(i['accNbr'])
		for code in range(len(phone) , step = -1):
			print phone[code]

