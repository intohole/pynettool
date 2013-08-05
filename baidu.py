#coding=utf-8




import util
 
suggesturl = 'http://esug.baidu.com/su?'
 
 
def suggest(word):
    query = {"wd":word,
             "p":3,
             "t":"1374026812745"}
    url = suggesturl + "wd=t&p=3&cb=window.bdsug.sug"
    print url 
#     url = util.queryurl(suggesturl, query)
    return util.get_url_data(url,"utf-8")
print suggest("天空")





    