# coding=utf-8
#!/usr/bin/env python


import urllib
import urllib2
import re
import sys
import cookielib
reload(sys)
sys.setdefaultencoding('utf-8')

lang_detect = re.compile("(charset\\s?=\\s?|encoding=\")([\w\d-]+)(\")?", re.IGNORECASE)


class UtilException(Exception):

    def __init__(self, msg, code=None):
        self.msg = msg
        self.code = code

    def __str__(self):
        if self.code:
            return "%s,%s" % (self.msg, self.code)
        else:
            return self.msg


class HtmlExtractException(UtilException):
    pass


class NoDataReturn(UtilException):
    pass


def get_url_reponse(baseurl, data=None, header={}):
    _response = None
    if baseurl:
        if not baseurl.endswith('?'):
            baseurl = baseurl + '?'
    req = urllib2.Request(baseurl)
    if header and isinstance(header, dict):
        for _key, _val in header.items():
            req.add_header(_key, _val)
    if data:
        if isinstance(data, dict):
            data = urllib.urlencode(data)
        _response = urllib2.urlopen(req, data)
    else:
        _response = urllib2.urlopen(req)
    return _response


def get_html_string(baseurl, data=None, header={}):
    __response = get_url_reponse(baseurl, data, header)
    __charset = __response.headers.getparam('charset')
    if header and not header.has_key('User-Agent'):
        header[
            'User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/30.0.1599.114 Chrome/30.0.1599.114 Safari/537.36'
    if __response:
        __html = __response.read()
        if not __charset or len(__charset) == 0:
            __charset = get_html_charset(__html)
        __html = __html.decode(__charset, 'ignore')
        return __html
    raise NoDataReturn, baseurl


def get_html_charset(html):
    __code = lang_detect.search(html)
    __codeing = "utf-8"
    if __code:
        __codeing = __code.group(2).strip()
        # __codeing = __code.split("charset=")[1].split("\"")[0]
    return __codeing


def set_urllib_proxy(protocol  , proxy_string):
    if not (protocol and isinstance(protocol ,(str)) and protocol.lower() in ['http' , 'https' , '' ]):
        raise TypeError,'protocol'
    if len(protocol) == 0:
        __proxy = urllib2.ProxyHandler({})
    else:
        __proxy = urllib2.ProxyHandler({protocol : proxy_string})
    urllib2.install_opener(__proxy)


def set_time_out(delay):
    urllib2.socket.setdefaulttimeout(delay)


def get_cookie(filename , method = 'save'):
    if method == save:
        __cookie = cookielib.FileCookieJar()
    pass

    

    

if __name__ == '__main__':
    print get_html_string('http://news.baidu.com')
