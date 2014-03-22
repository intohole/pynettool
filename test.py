#coding=utf-8



from pynettool.pynet import PyNet
from pynettool.chineseweather import ChineseWeather



p = PyNet()


print p.news()
print p.youdao_fanyi(q='word')

c = ChineseWeather()
for i in c.get_city_weather("江苏南京".encode("utf-8")):
        print i