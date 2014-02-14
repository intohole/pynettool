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
