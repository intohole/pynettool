#coding=utf-8
#!/usr/bin/env python



from utils  import network
from utils  import util
import json
import urllib



__net_dict = {'sina_ip':
                       {'query':{'format':'text'} , 'base_url' : 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?'} ,
              'youdao_ip':
                       {'query' : {'type':'ip'}  , 'base_url' :'http://www.youdao.com/smartresult-xml/search.s?'}
             }

class PyNet(object):

	def __get_response(self , url , **kw):
		http_get_url = url + self.__encode_params(**kw)
		__response = network.get_html_string(__callurl)
		if __response:
			return __response
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
			if __net_dict.has_key(key):
				if __net_dict[key].has_key('base_url'):
					__url = __net_dict[key]['base_url']
				else:
					raise Exception('%s not contain base_url' % key)
			else:
				raise Exception('%s can\'t find service' % key)
			if __net_dict['key'].has_key('query'):
				for __key , __val in __net_dict[key]['query'].items():
					kw[__kw] = __val 
			return self.__get_response(url = __url , **kw)
		return wrap


