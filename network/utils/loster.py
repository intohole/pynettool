#coding=utf-8
#!/usr/bin/env python




from utils  import network
from utils  import util

__sina_phone = 'http://php.tech.sina.com.cn/iframe/download/download_srv.php?action=bst_ms&code=%s&call_back=mobile_search_callback&_t=%d'



def get_phone(phone_num):
	__html = network.get_html_string(__sina_phone % ( phone_num , util.timems()))
	return __html

if __name__ == '__main__':
	print get_phone('18651856820')