# coding=utf-8
#!/usr/bin/env python


from utils import network
from utils import util


queryurl = "http://rate.tmall.com/listTagClouds.htm?"
detailurl = "http://rate.tmall.com/list_detail_rate.htm?"
suggesturl = "http://suggest.taobao.com/sug?"
commenturl = "http://rate.tmall.com/list_detail_rate.htm?"
iteminfo = "http://rate.tmall.com/list_dsr_info.htm?"
sellstatus = 'http://ext.mdskip.taobao.com/extension/dealRecords.htm?'

# 函数名称 consumer_opinion(itemid):
# 函数功能 获得淘宝客户的意见评论
# 参数：
#    itemid 淘宝商品id
# 返回：
#    json字符串 买家意见总结


def consumer_opinion(itemid):
    t = util.timems()
    query = {"itemId": itemid,
             "isAll": "true",
             "isInner": "true",
             "t": t,
             "_ksTS": "%s%s" % (t, util.randint(4)),
             "callback": "jsonp%s" % util.randint(4)}
    return network.get_html_string(queryurl, data=query)

#
#
# 买家评论列表
# 返回 json字符串
# itemid 商品id
# tagid 意见id
# page 页数
# posi
#


def consumer_comment(itemid, page, tagid='', posi=''):
    t = util.timems()
    query = {"itemId": itemid,
             "order": "1",
             "currentPage": page,
             "append": "0",
             "content": "1",
             "tagId": tagid,
             "posi": posi,
             "_ksTS": "%s%s" % (t, util.randint(4)),
             "callback": "jsonp1753"}
    return network.get_html_string(detailurl, data=query)


def get_comment(itemid, page, order=1, content=1, append=''):
    query = {"itemId": itemid,
             "order": order,
             "currentPage": page,
             "append": append,
             "content": content,
             "_ksTS": util.getksTs(),
             "callback": util.getJsonp()}
    url = util.queryurl(commenturl, query)
    return network.get_html_string(url)
# 淘宝建议
# word 任意字符串
# 返回
#    json字符串


def suggest(word):
    query = {
        "code": "utf-8",
        "q": word,
        "_ksTS": util.getksTs(),
        "callback": util.getJsonp(),
        "k": "1"}
    return network.get_html_string(baseurl=suggesturl, data=query)


def getsellstatus(itemid):
    query = {"itemid": itemid,
             "callback": "TShop.mods.DealRecord.reload"}
    url = util.queryurl(suggesturl, query)
    return network.get_html_string(url)


def list_dsr(itemid):
    query = {"itemId": itemid,
             "_ksTS": util.getksTs(),
             "callback": util.getJsonp()}
    url = util.queryurl(iteminfo, query)
    return network.get_html_string(url)


def getjson(data):
    data = data[13:len(data) - 1]
    return data


def getcommentinfo(tagdict):
    if not isinstance(tagdict, dict):
        return None
    if tagdict.has_key("tags"):
        if tagdict["tags"].has_key("tagClouds"):
            taglist = []
            for tag in tagdict["tags"]["tagClouds"]:
                if tag["posi"]:
                    tag["posi"] = 1
                else:
                    tag["posi"] = -1
                taglist.append(
                    (tag["id"], long(tag["count"]) / 20 + 1, tag["posi"], tag["tag"]))
            return taglist
    return None


def commentlist(itemid, page, tagid='', posi=''):
    d = util.jsonstrtodict(
        util.getjson(consumer_comment(itemid, page, tagid, posi)))
    try:
        if d and d.has_key("rateDetail"):
            rateList = None
            pageRemain = 0
            if d["rateDetail"].has_key("rateList"):
                rateList = d["rateDetail"]["rateList"]
            if d["rateDetail"].has_key('paginator'):
                pageRemain = d["rateDetail"]['paginator'][
                    'lastPage'] - d["rateDetail"]['paginator']['page']
            return (pageRemain, rateList)
    except Exception, e:
        print e, d
        return None


from BeautifulSoup import BeautifulSoup


class JDComment(object):

    def __down_load(self, item, page):
        return network.get_html_string('http://club.jd.com/review/%s-0-%s-0.html' % (item, page))

    def get_comment(self, item):
        html = self.__down_load(item, 1)
        # print html
        soup = BeautifulSoup(html)
        if soup:
            for l in soup.find_all(attrs={'class': 'u-con'}):
                print l.string

    def __getattr__(self, key):

        return network.get_html_string('http://club.jd.com/review/1006105-0-54-0.html')


if __name__ == "__main__":
    # print consumer_comment(38134348913, 230)
    with open('/home/lixuze/phone.txt', 'a') as f:
        for itemid in set(['36779353822', '35392148256', '38246437750',
                       '36936854745', '38357600011', '38223792308', '38134348913',
                       '37739448829', '37352068995', '37395195418', '27332632677', '19659690261', '36135293856']):

            pageRemain = 1
            while True:
                print '%s  %s ' % (itemid, pageRemain)
                result = commentlist(itemid, pageRemain, '', '')
                if not result:
                    break
                if result[0] > 0:
                    pageRemain += 1
                else:
                    break
                if result[1]:
                    for i in result[1]:
                        f.write('%s\n' % i['rateContent'])
                else:
                    break
