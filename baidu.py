#coding=utf-8




import util
 
suggesturl = 'http://esug.baidu.com/su?'
 
 
def suggest(word):
    query = {"wd":word,
             "p":3,
             "t":util.timems()}
    url = util.queryurl(suggesturl, query)
    return util.get_url_data(url,"")

if __name__ == "__main__":
    pass





    