pynettool说明
====================

+收集网络接口 ， 方便pythonic 使用

天气接口
------------------------
:::python
    
    from pynettool.chineseweather import ChineseWeather
    c = ChineseWeather()
    print c.getweatherdata('江苏南京'.encode('utf-8')) #一个城市的天气数据
    print c.getsk('江苏南京'.encode('utf-8')) #实况天气信息 返回是个词典　格式简单　自己解析吧
    #get_city_weather 支持任何一个城市 格式 省份 市 区县 特殊情况 上海 上海 则为上海
    for i in c.get_city_weather("江苏南京江宁".encode("utf-8")):
        print i 


百度商情接口
-------------------------
:::python
     
    import pynettool.baidubuinese as bd
    if __name__ == "__main__":
    print bd.get_buinese_releate("三星"  ) 
    print bd.get_search_num('三星')
    print bd.get_area_info('三星' , 10 )


pynet 接口
------------------------------
:::python
  
     
     from pynettool.pynet import PyNet

     if __name__ == '__main__':
          p = PyNet()
          print p.baidu_search_num(word='htc') #查询百度搜索词的次数
          print p.baidu_releate(word='htc') #查询相关查询
          print p.baidu_area_num(word='htc', num=10, areaid='') #查询搜索词区域数目
          print p.sina_ip(ip='220.181.111.86') #查询ip信息 
          print p.sina_phone(m='13833445577') #查询电话信息
          print p.youdao_fanyi(q = 'word') #有道翻译接口
          print p.baidu_suggest(wd='天气' , _ = util.timems()) #百度建议词接口
          print p.kuaidi(type = 'shunfeng' , postid = '574869634762') # 快递接口查询 type : 快递名称 , postid : 快递单号 type {'shentong' : '申通' , 'shunfeng' : '顺风' , 'huitongkuaidi' : '汇通快递' , 'zhongtong' : '中通' , 'yunda' : '韵达'} ....更多快递名称你发现
          print p.news() # 新闻获得
          print p.xunlei(url='thunder://QUFmdHA6Ly91OnVAZDMuZGwxMjM0LmNvbTo4MDA2L1vnlLXlvbHlpKnloIJ3d3cuZHkyMDE4LmNvbV3lrrblm63pmLLnur9IROiLseivreS4reWtly5ybXZiWlo=/') # url = 迅雷地址 迅雷地址转换
          print p.xuanfeng(url = 'qqdl://ZnRwOi8vZHlnb2QxOmR5Z29kMUBkMDE4LmR5Z29kLm5ldDo4ODU4L+mbqueLl+WFhOW8ny9b55S15b2x5aSp5aCCd3d3LmR5Z29kLm5ldF3pm6rni5flhYTlvJ9EVkQucm12Yg==') # url = 旋风地址 旋风地址转换
          print p.dianxin_phone(areaCode = '025' ,  areaId = '10') # 电信电话号码查询 areaCode 区号 areaId  地区编号 (showCount 展示数目)
          print p.howold(t = '1992/02/03').year #你想知道你现在多大了吗　试试这个　输入你的生日 格式 :(1992年10月20号  ,1992/02/04 ,1992-03-04)  你会获得你存在的小时(hour)　分钟(minute)　天数(day) 年(year)




loster.py 空气质量接口pm25.in 网站接口
-----------------
:::python
     
     from pynettool.loster import PM25
     p = PM25(base_url = 'http://www.pm25.in/api/querys/' , token  = '5j1znBVAsnSf5xQyNQyq')
    print p.pm2_5(city = '南京')