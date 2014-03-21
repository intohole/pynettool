# coding=utf-8


import json
import random
import time
import re
import base64





_jload = json.loads
lang_detect = re.compile("<meta(.+?)\charset=[a-zA-Z0-9]+\">", re.IGNORECASE)


def jsonstrtodict(jsonstr):
    datadict = None
    try:
        datadict = _jload(jsonstr)
    except Exception, e:
        raise TaoBaoException("JSON_DECODE_ERRO_%s" % e, 102)
    return datadict


'''
函数名称： randint
函数功能： 随机生成n位随机数
参数列表：
       n 随机生成的位数
返回值：
       整数型
'''


def randint(n):
    _num = 1
    if n > 1:
        for i in range(n - 1):
            _num *= 10
    else:
        raise TaoBaoException("NO_RIGHT_NUM", 110)
    return random.randint(_num, (_num * 10) - 1)


def randintbyrang(_min, _max):
    if _min >= _max:
        raise TaoBaoException("VALUE_IS_NOT_VALUE", 113)
    return random.randint(_min, _max)




def timems():
    return long(time.time()) * 1000


def getksTs():
    return "%s_%s" % (timems(), randint(4))


def getJsonp():
    return "jsonp%s" % (randint(4))

'''
功能：
    从一个含有json字符串中，提取json字符串（jsonp({"1":2})）
返回：
    json字符串 成功
    ValueError: substring not found 异常
原理：
    
'''


def getjson(data):
    return data[data.index("{"):data.rindex("}") + 1]


def xunlei(**kw):
    
    if kw.has_key('url'):
        url = kw['url']
    else:
        return ''
    if url and isinstance(url , (str , unicode)) and url.startswith('thunder://'):
        __url = base64.decodestring(url[10:])
        #去除掉迅雷 AA***ZZ
        return __url[2:-2]


def xuanfeng(**kw):
    if kw.has_key('url') : 
        if kw['url'] and isinstance(kw['url'] , (str, unicode)) and kw['url'].startswith('qqdl://'):
            return base64.decodestring(kw['url'].decode('utf-8')[7:])
        return ''




if __name__ == "__main__":
    print xunlei(url = 'thunder://QUFmdHA6Ly91OnVAZDMuZGwxMjM0LmNvbTo4MDA2L1vnlLXlvbHlpKnloIJ3d3cuZHkyMDE4LmNvbV3lrrblm63pmLLnur9IROiLseivreS4reWtly5ybXZiWlo=/')
    print xuanfeng(url = 'qqdl://ZnRwOi8vZHlnb2QxOmR5Z29kMUBkMDE4LmR5Z29kLm5ldDo4ODU4L+mbqueLl+WFhOW8ny9b55S15b2x5aSp5aCCd3d3LmR5Z29kLm5ldF3pm6rni5flhYTlvJ9EVkQucm12Yg==')