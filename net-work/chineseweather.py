#coding=utf-8


import util 
from Trie import Trie
from taobaoexception import TaoBaoException


class ChineseWeather(object):
    
    _trie = Trie()
    
    def __init__(self):
        self.load_city_id()
    
    def load_city_id(self):
        filehandle= open("./weather.txt", mode='r')
        contents = filehandle.readlines()
        for line in contents:
            line = line.strip()
            if line and line != "":
                idArry = line.split("#")
                _cityname = ''
                _id = idArry[0]
                if len(idArry) == 4:
                    if idArry[3] == idArry[2] == idArry[1]:
                        _cityname = idArry[3].strip()
                    elif idArry[3] == idArry[2] != idArry[1]:
                        _cityname = idArry[2].strip() + idArry[1].strip()
                    else:
                        _cityname = idArry[3].strip() + idArry[2].strip() + idArry[1].strip()
                self._trie.add(_cityname, _id)
        filehandle.close()
    def _get_city_id(self, cityname , splitword = ' '):
        if not cityname and cityname.strip()=="":
            raise  TaoBaoException("INPUT_CITY_NAME_IS_NONE_OR_EMPTY",301)
        _searchword = ''
        for word in cityname.split(splitword):
            _searchword = _searchword + word.strip()
        return self._trie.search(_searchword)
    
    def get_city_weather(self , cityname):
        _id = self._get_city_id(cityname)
        if _id[1]:
            url = 'http://m.weather.com.cn/data/%s.html' % _id[1]
            return self._get_id(url)
                    
    
    def _get_id(self,url):
        query =  {}
        return util.get_url_info(query, url)

if __name__ == "__main__":
    c = ChineseWeather()
    print c.get_city_weather("北京海")