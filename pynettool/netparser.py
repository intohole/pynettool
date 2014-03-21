#coding=utf-8
#!/usr/bin/env python



#1	220.181.0.0	220.181.255.255	中国	北京	北京		电信		北京蓝汛通信专属电信
def sina_ip(result):
	def parser():
		if result and len(result) > 0:
			result_arry = result.split('\t')
			if len(result_arry) >= 8:
				return dict(country = result_arry[3] , province = result_arry[4] , city = result_arry[5] , server =result_arry[7] , belong = result_arry[9])
			print 'xx'
	return parser

if __name__== '__main__':
	for __key , __value in  sina_ip('1	220.181.0.0	220.181.255.255	中国	北京	北京		电信		北京蓝汛通信专属电信')().items():
		print __key , __value
