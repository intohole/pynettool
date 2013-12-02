#coding=utf-8




import network
import util


queryurl = "http://rate.tmall.com/listTagClouds.htm?"
detailurl = "http://rate.tmall.com/list_detail_rate.htm?"
suggesturl = "http://suggest.taobao.com/sug?"
commenturl = "http://rate.tmall.com/list_detail_rate.htm?"
iteminfo = "http://rate.tmall.com/list_dsr_info.htm?"
sellstatus = 'http://ext.mdskip.taobao.com/extension/dealRecords.htm?'

#函数名称 consumer_opinion(itemid):
#函数功能 获得淘宝客户的意见评论
#参数：
#    itemid 淘宝商品id
#返回：
#    json字符串 买家意见总结
def consumer_opinion(itemid):
    t = util.timems()
    query = {"itemId":itemid,
             "isAll":"true",
             "isInner":"true",
             "t":t,
             "_ksTS":"%s%s" % (t,util.randint(4)),
             "callback":"jsonp%s" % util.randint(4)}
    url = util.queryurl(queryurl , query)
    return network.get_html_string(url)

#
#
#买家评论列表
#返回 json字符串
# itemid 商品id
# tagid 意见id
# page 页数
# posi
#
def consumer_comment(itemid,tagid,page,posi):
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
    return network.get_html_string(url)


def get_comment(itemid,page,order=1,content=1,append=''):
    query = {"itemId":itemid,
             "order":order,
             "currentPage":page,
             "append":append,
             "content":content,
             "_ksTS":util.getksTs(),
             "callback":util.getJsonp()}
    url = util.queryurl(commenturl, query)
    return network.get_html_string(url)
#淘宝建议
# word 任意字符串
# 返回 
#    json字符串

def suggest(word):
    query = {
             "code":"utf-8",
             "q":word,
             "_ksTS":util.getksTs(),
             "callback":util.getJsonp(),
             "k":"1"}
    url = util.queryurl(suggesturl, query)
    return network.get_html_string(url)


def getsellstatus(itemid):
    query = {"itemid":itemid,
             "callback":"TShop.mods.DealRecord.reload"}
    url = util.queryurl(suggesturl, query)
    return network.get_html_string(url)

def list_dsr(itemid):
    query = {"itemId":itemid,
             "_ksTS":util.getksTs(),
             "callback":util.getJsonp()}
    url = util.queryurl(iteminfo, query)
    return network.get_html_string(url)
       
    
def getjson(data):
    data = data[13:len(data)-1]
    return data


          

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
    d = util.jsonstrtodict(util.getjson(consumer_opinion(itemid,tagid,page,posi)))
    try:
        if  d and d.has_key("rateDetail"):
            if d["rateDetail"].has_key("rateList"):
                return d["rateDetail"]["rateList"]
    except Exception,e:
        print e,d
        return None
    

if __name__ == "__main__":
    print suggest('天')    