#coding=utf-8

import util



class Query(object):
    
    __dict__ = {} #词典    
    _querystring = "" #保存的query字符串
    
    
    def __setattr__(self,attr,val):
        self.__dict__[attr] = val

    def toDict(self):
        return self.__dict__

    def initWithDict(self,datadict):
        for _key,_value in datadict.items():
            setattr(self, _key, _value)
    
    def toQuery(self):
        if self._querystring == "":
            self._querystring = util._urlencode(self.__dict__)
        return self.querystring

    
    
                
    