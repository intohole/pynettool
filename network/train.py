#coding=utf-8
#!/usr/bin/env python

import util
import json


train_url = "http://train.qunar.com/qunar/stationtostation.jsp?"

def train(_from , _dest):
    query = {"format":"json",
             "from":_from,
             "to":_dest,
             "type":"oneway",
             "date":"20131016",
             "ver":"1381732624162",
             "ex_track":"",
             "cityname":"123456",
             "callback":"XQScript_5"}
    
    return util.getjson(util.get_url_html_string(query, train_url))

if __name__ == "__main__":
    for _key,_val in  json.loads(train("北京" , "武汉")).items():
        print _key,_val

