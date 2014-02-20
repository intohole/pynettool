#coding=utf-8
#!/usr/bin/env python




from utils  import network
from utils  import util
import json

__sina_phone = 'http://api.showji.com/Locating/www.showji.co.m.aspx?m=%s&output=json'





def get_phone(phone_num):
	class moblie(object):
		phone = ''
		province = ''
		city = ''
		areacode = ''
		phone_type = ''
		post_code = ''
	__html = network.get_html_string(__sina_phone % ( phone_num))
	__result_dict = json.loads(__html)
	result = moblie()
	result.phone = __result_dict['Mobile']
	result.province = __result_dict['Province']
	result.city = __result_dict['City']
	result.areacode = __result_dict['AreaCode']
	result.phone_type = __result_dict['Corp']
	result.post_code = __result_dict['PostCode']
	return result


if __name__ == '__main__':
	print get_phone('18651856820').phone