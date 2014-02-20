#coding=utf-8
#!/usr/bin/env python




from utils  import network
from utils  import util
import json
import urllib

__sina_phone = 'http://api.showji.com/Locating/www.showji.co.m.aspx?m=%s&output=json'
__air_quality = 'http://www.pm25.in/api/querys/pm2_5.json?token=5j1znBVAsnSf5xQyNQyq&city=%s'


class NetException(Exception):
	pass


		

class PM25(object):
	def __init__(self , base_url = 'http://www.pm25.in/api/querys/' , token = '5j1znBVAsnSf5xQyNQyq'):
		self.__base_url = base_url 
		self.__token = token

	def set_token(self , token):
		self.__token = token

	def get_json(self ,url , **kw):
		kw['token'] = self.__token
		__callurl = url + self.__encode_params(**kw)
		__response = network.get_html_string(__callurl)
		if __response:
			return json.loads(__response)
		else:
			raise NetException,__callurl

	def __encode_params(self,**kw):
	    args = []
	    for k, v in kw.iteritems():
	        qv = v.encode('utf-8') if isinstance(v, unicode) else str(v)
	        args.append('%s=%s' % (k, urllib.quote(qv)))
	    return '&'.join(args)

	def __getattr__(self , key ):
		def wrap(**kw):
			__url = ''.join([self.__base_url , key , '.json?'])
			return self.get_json(url = __url , **kw)
		return wrap



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
	p = PM25(base_url = 'http://www.pm25.in/api/querys/' , token  = '5j1znBVAsnSf5xQyNQyq')
	print p.pm2_5(city = '南京')