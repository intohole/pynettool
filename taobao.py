#coding=utf-8




import json
import time
import util

queryurl = "http://rate.tmall.com/listTagClouds.htm?"
detailurl = "http://rate.tmall.com/list_detail_rate.htm?"
suggesturl = "http://suggest.taobao.com/sug?"
commenturl = "http://rate.tmall.com/list_detail_rate.htm?"
iteminfo = "http://rate.tmall.com/list_dsr_info.htm?"
sellstatus = 'http://ext.mdskip.taobao.com/extension/dealRecords.htm?'

def makequery(itemid):
    t = util.timems()
    query = {"itemId":itemid,
             "isAll":"true",
             "isInner":"true",
             "t":t,
             "_ksTS":"%s%s" % (t,util.randint(4)),
             "callback":"jsonp%s" % util.randint(4)}
    url = util.queryurl(queryurl , query)
    return util.get_url_data(url, codemode = "gbk")

def makecomment(itemid,tagid,page,posi):
    query = {"itemId":itemid,
             "order":"1",
             "currentPage":page,
             "append":"0",
             "content":"1",
             "tagId":tagid,
             "posi":posi,
             "_ksTS":"1373940680057_1752",
             "callback":"jsonp1753"}
    url = util.queryurl(detailurl, query)
    return util.get_url_data(url, codemode = "gbk")

def get_comment(itemid,page,order=1,content=1,append=''):
    query = {"itemId":itemid,
             "order":order,
             "currentPage":page,
             "append":append,
             "content":content,
             "_ksTS":util.getksTs(),
             "callback":util.getJsonp()}
    url = util.queryurl(commenturl, query)
    return util.get_url_data(url)

def suggest(word):
    query = {
             "code":"utf-8",
             "q":word,
             "_ksTS":util.getksTs(),
             "callback":util.getJsonp(),
             "k":"1"}
    url = util.queryurl(suggesturl, query)
    return util.get_url_data(url, codemode = "utf-8")


def getsellstatus(itemid):
    query = {"itemid":itemid,
             "callback":"TShop.mods.DealRecord.reload"}
    url = util.queryurl(suggesturl, query)
    return util.get_url_data(url)

def list_dsr(itemid):
    query = {"itemId":itemid,
             "_ksTS":util.getksTs(),
             "callback":util.getJsonp()}
    url = util.queryurl(iteminfo, query)
    return util.get_url_data(url)
       
    
def getjson(data):
    data = data[13:len(data)-1]
    return data


def jsonstrtodict(jsonstr):
    datadict = None
    try:
        datadict = json.loads(jsonstr)
    except Exception,e:
        print e
    return datadict                

def getcommentinfo(tagdict):
    if not isinstance(tagdict,dict):
        return None
    if tagdict.has_key("tags"):
        if tagdict["tags"].has_key("tagClouds"):
            taglist = []
            for tag in tagdict["tags"]["tagClouds"]:
                if tag["posi"]:
                    tag["posi"] = 1
                else:
                    tag["posi"] = -1
                taglist.append((tag["id"],long(tag["count"]) / 20 + 1,tag["posi"],tag["tag"]))
            return taglist
    return None

def commentlist(itemid,tagid,page,posi):
    d = jsonstrtodict(getjson(makecomment(itemid,tagid,page,posi)))
    try:
        if  d and d.has_key("rateDetail"):
            if d["rateDetail"].has_key("rateList"):
                return d["rateDetail"]["rateList"]
    except Exception,e:
        print e,d
        return None
def writefile(filepath,data,mode = "a"):
    fileHandle = open(filepath,mode)
    fileHandle.write(data + "\n")
    fileHandle.close()        


def save(itemid):
    for tag in getcommentinfo(jsonstrtodict(getjson(makequery(itemid)))):
        time.sleep(1)
        for i in range(1,tag[1]+1):
            d = commentlist(itemid,tag[0],i,tag[2])
            if  d:
                for comment in d:
                    writefile("/home/lixuze/phone/_%s" % tag[3],"%s##%s" %(comment["position"] , comment["rateContent"]))

print getsellstatus(19399255654)    