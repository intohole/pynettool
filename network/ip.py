#coding=utf-8
#!/usr/bin/env python



from utils import network


__sina_ip = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=text&ip=%s'
__youdao_ip = 'http://www.youdao.com/smartresult-xml/search.s?type=ip&q=%s'

def __get_ip_location(ip , base_url):
	if ip and isinstance(ip, (str , unicode)) or ip =='':
		return network.get_html_string( base_url % ip)
	raise Exception('ip is not string or unicode')

def get_ip_location_sina(ip):
	return __get_ip_location(ip , __sina_ip)


def get_ip_location_youdao(ip):
	return __get_ip_location(ip , __youdao_ip)


def get_ip_local():
	return __get_ip_location('' , __sina_ip)



if __name__ == '__main__':
	print get_ip_location_youdao('220.181.111.86')