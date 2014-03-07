# coding=utf-8
#!/usr/bin/env python


from utils import network
from utils import util
import json
import urllib
import time

_net_dict = {'sina_ip':
            {'query': {'format': 'text'}, 'base_url':
             'http://int.dpool.sina.com.cn/iplookup/iplookup.php?'},
             'youdao_ip':
            {'query': {'type': 'ip'}, 'base_url':
             'http://www.youdao.com/smartresult-xml/search.s?'},
             'baidu_releate':
            {'query': {}, 'base_url':
             'http://shangqing.baidu.com/trade/wordPv_view.htm?'},
             'baidu_search_num':
            {'query': {}, 'base_url':
             'http://shangqing.baidu.com/trade/wordPv_statistics.htm?'},
             'baidu_area_num':
            {'query': {'areaid': ''}, 'base_url':
             'http://shangqing.baidu.com/recomword/recomWordCache_findProvPvCache.htm?'},
             'sina_phone':
            {'query': {'output': 'json'}, 'base_url':
             'http://api.showji.com/Locating/www.showji.co.m.aspx?'},
             'baidu_suggest':
             {'query': {'sid': '', '_': util.timems},
                 'base_url': 'http://suggestion.baidu.com/su?'},
             'youdao_fanyi':
             {'query': {'keyfrom': 'tinxing', 'key': '1312427901', 'type': 'data', 'doctype':
                        'json', 'version': '1.1'}, 'base_url': 'http://fanyi.youdao.com/openapi.do?'},
             'kuaidi':
             {'base_url': 'http://baidu.kuaidi100.com/query?'},
             'news':
             {'query': {"category": "__all__",
                        "count": "20",
                        "offset": "0",
                        "utm_source": "toutiao",
                        }, 'base_url': 'http://www.toutiao.com/api/article/recent/?'},
             'xunlei':
            {'call_back': util.xunlei},
            'xuanfeng':
            {'call_back' : util.xuanfeng},
             'dianxin_phone':
            {'query': {"areaId": "10",
                       "areaCode": "025",
                       "numberHead": "",
                       "showCount": "16",
                       "isFour": "",
                       "matchNum": "tailNotFour",
                       "numberFee": "",
                       "maxStoredCalls": "",
                       "numTypeReg": ""}, 'base_url':
                'http://js.189.cn/nmall/shop/number/queryNumber.json?'}

             }


class PyNet(object):

    __get_rule = {}

    def __init__(self, rule_dict=_net_dict):
        if rule_dict and isinstance(rule_dict, dict):
            self.__get_rule = rule_dict.copy()
        else:
            self.__get_rule = _net_dict.copy()

    def add_rule(self, rule):
        if rule and isinstance(rule, dict):
            for __name, __rule in rule.items():
                if self.__get_rule.has_key(__name) or not __rule or not isinstance(__rule, dict):
                    continue
                if (rule[__name].has_key('base_url') and isinstance(rule['base_url'], (str, unicode))) or rule[__name].has_key('call_back'):
                    self.__get_rule[__name] = __rule
        else:
            raise TypeErro(
                'rule must be dict eg. {xx:{\'query\' :{} , \'base_url\' : \'xxx\'} }')

    def __get_response(self, url, **kw):
        http_get_url = url + self.__encode_params(**kw)
        __response = network.get_html_string(http_get_url)
        if __response:
            return __response
        else:
            raise NetException, __callurl

    def __encode_params(self, **kw):
        args = []
        for k, v in kw.iteritems():
            if callable(v):
                v = v()
            qv = v.encode('utf-8') if isinstance(v, unicode) else str(v)
            args.append('%s=%s' % (k, urllib.quote(qv)))
        return '&'.join(args)

    def __getattr__(self, key):
        def wrap(**kw):
            if self.__get_rule.has_key(key):
                if self.__get_rule[key].has_key('call_back'):
                    return self.__get_rule[key]['call_back'](**kw)
                if self.__get_rule[key].has_key('base_url'):
                    __url = self.__get_rule[key]['base_url']
                else:
                    raise Exception('%s not contain base_url' % key)
            else:
                raise Exception('%s can\'t find service' % key)
            if self.__get_rule[key].has_key('query'):
                for __key, __val in self.__get_rule[key]['query'].items():
                    kw[__key] = __val
            return self.__get_response(url=__url, **kw)
        return wrap


if __name__ == '__main__':
    p = PyNet()
    print p.baidu_search_num(word='htc')
    print p.baidu_releate(word='htc')
    print p.baidu_area_num(word='htc', num=10, areaid='')
    print p.sina_ip(ip='220.181.111.86')
    print p.sina_phone(m='13833445577')
    print p.baidu_suggest(wd='天气')
    print p.youdao_fanyi(q='word')
    print p.kuaidi(type='huitongkuaidi', postid='350146137409')
    print p.kuaidi(type='shentong', postid='768089232106')
    print p.kuaidi(type='shunfeng', postid='574869634762')
    print p.news()
    print p.xunlei(url='thunder://QUFmdHA6Ly91OnVAZDMuZGwxMjM0LmNvbTo4MDA2L1vnlLXlvbHlpKnloIJ3d3cuZHkyMDE4LmNvbV3lrrblm63pmLLnur9IROiLseivreS4reWtly5ybXZiWlo=/')
    print p.xuanfeng(url = 'qqdl://ZnRwOi8vZHlnb2QxOmR5Z29kMUBkMDE4LmR5Z29kLm5ldDo4ODU4L+mbqueLl+WFhOW8ny9b55S15b2x5aSp5aCCd3d3LmR5Z29kLm5ldF3pm6rni5flhYTlvJ9EVkQucm12Yg==')
    print p.dianxin_phone(areaCode = '025' ,  areaId = '10')
