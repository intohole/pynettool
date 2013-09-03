#coding=utf-8

from network import util
import re

root_url = 'http://w.mail.qq.com'
redirect = re.compile("<meta http-equiv=\"Refresh\" content=\"1;url=(.*)\"/>")
bottle_pattern = re.compile("<a href=\"/cgi-bin/bottle_list[^>]*>")


class QQBottele(object):
    current_html = None
    def do_login(self, username , password):
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
            self.current_html = util.get_url_data(_url,codemode="utf-8")
            
            
    def open_bottle(self):
        if self.current_html and self.current_html !='':
            m = bottle_pattern.search(self.current_html)
            if m:
                self.current_html = util.get_url_data(root_url + m.group().split("\"")[1] , codemode="gbk")
                print self.current_html

if __name__ == "__main__":
    q = QQBottele()
    
    
    

