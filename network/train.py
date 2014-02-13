#coding=utf-8
#!/usr/bin/env python

import util
import network


train_url = "http://train.qunar.com/qunar/stationtostation.jsp?"

def train(_from , _dest):
    query = {"format":"json",
             "from":_from,
             "to":_dest,
             "type":"oneway",
             "date":"20131016",
             "ver":util.timems(),
             "ex_track":"",
             "cityname":"123456",
             "callback":"XQScript_5"}
    
    return util.getjson(network.get_html_string(train_url, query))

if __name__ == "__main__":
    print util.jsonstrtodict(train("北京" , "武汉"))
