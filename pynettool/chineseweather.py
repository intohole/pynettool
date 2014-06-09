#coding=utf-8



from utils import util
from utils import Trie
from utils import network
import json
import os

week_name = ( '一' , '二' , '三' , '四' , '五' , '六' , '日')
week_dict = {'一' :  0 , '二' : 1 , '三' : 2 , '四' : 3 , '五' : 4 , '六' : 5 , '天':6 }

class WeatherInfo(object):
    week = '' #周几
    temp = '' #温度
    date = '' #日期
    city = '' #城市名称
    wind = '' #风力
    weather = '' #天气情况

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.week , self.temp , self.date , self.city , self.wind , self.weather )

class ChineseWeather(object):

    __trie = Trie.Trie()

    def __init__(self):
        self.load_city_id()

    def load_city_id(self):
        __content = []
        __weather__file = os.path.join(os.path.abspath(os.path.dirname(__file__)) , 'data/weather.txt')
        with open(__weather__file) as f:
            __content.extend([line.strip() for line in f.readlines()])
        for line in __content:
            weather_info = line.split('#')
            if len(weather_info) == 4:
                __city_name = []
                if weather_info[3] == weather_info[2] == weather_info[1]:
                    __city_name.append(weather_info[3])
                elif weather_info[2] == weather_info[1]:
                    __city_name.extend([weather_info[3] , weather_info[1]])
                else:
                    __city_name.extend([weather_info[3] , weather_info[2] , weather_info[1]])
                self.__trie.add(''.join(__city_name) , weather_info[0])


    def get_city_id(self, cityname , splitword = ' '):
        if not cityname and cityname.strip()=="":
            raise  Exception("INPUT_CITY_NAME_IS_NONE_OR_EMPTY")
        __searchword = ''.join(cityname.split(splitword))
        return self.__trie.search(__searchword)

    def get_city_weather(self , cityname):
        __city_id = self.get_city_id(cityname)
        if __city_id[1]:
            url = 'http://m.weather.com.cn/data/%s.html' % __city_id[1]
            return self.parser_to_string(network.get_html_string(url , {}))
        return None


    def parser_to_string(self , html):
        __weather_json = json.loads(html)
        __weather_arry = []
        __week_index = week_dict[__weather_json['weatherinfo']['week'].split('星期')[1].encode('utf-8')]
        for i in range(6):
            __weather_arry.append(WeatherInfo())
            __weather_arry[i].city = __weather_json['weatherinfo']['city']
            __weather_arry[i].week = '周%s' % week_name[ ((__week_index + i) % 7) ]
            __weather_arry[i].temp = __weather_json['weatherinfo']['temp%d' % (i+1) ]
            __weather_arry[i].date = __weather_json['weatherinfo']['date_y']
            __weather_arry[i].wind = __weather_json['weatherinfo']['wind%d' % (i+1) ]
            __weather_arry[i].weather = __weather_json['weatherinfo']['weather%d' % (i+1) ]
        return __weather_arry


    def getsk(self , cityname):
        __city_id = self.get_city_id(cityname)
        if __city_id and __city_id[1]:
            __url = 'http://www.weather.com.cn/data/sk/%s.html' % __city_id[1]
            return json.loads( network.get_html_string(__url , {}) )
        return None


    def getweatherdata(self , cityname):
        __city_id = self.get_city_id(cityname)
        if __city_id and __city_id[1]:
            __url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % __city_id[1]
            return json.loads( network.get_html_string(__url , {}) )
        return None





if __name__ == "__main__":
    c = ChineseWeather()
    print c.getweatherdata('江苏南京'.encode('utf-8'))
    print c.getsk('江苏南京'.encode('utf-8'))
    for i in c.get_city_weather("江苏南京".encode("utf-8")):
        print i

