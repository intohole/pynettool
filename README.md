pynettool说明
====================

+收集网络接口 ， 方便pythonic 使用

天气接口
------------------------
:::python
    
    from chineseweather import ChineseWeather
    c = ChineseWeather()
    #get_city_weather 支持任何一个城市 格式 省份 市 区县 特殊情况 上海 上海 则为上海
    for i in c.get_city_weather("江苏南京江宁".encode("utf-8")):
        print i 


百度商情接口
-------------------------
:::python
     
    import baidubuinese as bd
    if __name__ == "__main__":
    print bd.get_buinese_releate("三星"  ) 
    print bd.get_search_num('三星')
    print bd.get_area_info('三星' , 10 )


pynet 接口
------------------------------
:::python
  
     from pynet import PyNet
     if __name__ == '__main__':
          p = PyNet()
          print p.baidu_search_num(word='htc') #查询百度搜索词的次数
          print p.baidu_releate(word='htc') #查询相关查询
          print p.baidu_area_num(word='htc', num=10, areaid='') #查询搜索词区域数目
          print p.sina_ip(ip='220.181.111.86') #查询ip信息 
          print p.sina_phone(m='13833445577') #查询电话信息


loster.py 空气质量接口pm25.in 网站接口
-----------------
:::python
     
     from loster import PM25
     p = PM25(base_url = 'http://www.pm25.in/api/querys/' , token  = '5j1znBVAsnSf5xQyNQyq')
    print p.pm2_5(city = '南京')