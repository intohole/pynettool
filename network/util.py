# coding=utf-8


from taobaoexception import TaoBaoException
import json
import random
import time
import re


code = {"gbk": "gbk",
        "utf-8": "utf-8",
        "gb2312": "gb2312"}


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


if __name__ == "__main__":
    for _key, _val in jsonstrtodict("""{"ret":1,"start":"58.240.48.0","end":"58.240.159.255","country":"\u4e2d\u56fd","province":"\u6c5f\u82cf","city":"\u5357\u4eac","district":"","isp":"\u8054\u901a","type":"","desc":""}""").items() :
        if isinstance(_val, (unicode, str)):
            print _val.encode('utf-8')
        else:
            print _val
