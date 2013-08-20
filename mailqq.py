#coding=utf-8

from network import util
import re
import urllib2

redirect = re.compile("<meta http-equiv=\"Refresh\" content=\"1;url=(.*)\"/>")


def do_login(username , password):
    data = {'f':'xhtmlmp',
            'delegate_url':'',
            'f':'xhtmlmp',
            'action':'',
            'tfcont':'',
            'uin':username,
            'aliastype':'@qq.com',
            'pwd':password,
            'mss':'1',
            'mtk':'',
            'btlogin':''}
    header = {'Referer':'http://w.mail.qq.com/cgi-bin/loginpage?t=loginpage&s=logout&f=xhtmlmp&autologin=n',
              'Host':'w.mail.qq.com',
              'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    html = util._get_url_data('http://w.mail.qq.com/cgi-bin/login', data, header,"utf-8")
    m = redirect.search(html)
    _url = None
    if m:
        print m.group()
        _url = m.group().split("url=")[1].split("\"")[0]
    if _url:
        print util.get_url_data(_url,codemode="utf-8")
    

