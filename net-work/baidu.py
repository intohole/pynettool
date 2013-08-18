# coding=utf-8



import threading
import util
 
suggesturl = 'http://esug.baidu.com/su?'
ip_url = "http://opendata.baidu.com/api.php?"
 
def get_suggest_word(word):
    query = {"wd":word,
             "p":3,
             "t":util.timems()}
    url = util.queryurl(suggesturl, query)
    return util.get_url_data(url, "")

def get_bd_ip_local(ip):
    query = {"query":ip,
            "co":"",
            "resource_id":"6006",
            "t":"1376035704061",
            "ie":"utf8",
            "oe":"gbk",
            "cb":"bd__cbs__yk2g9h",
            "format":"json",
            "tn":"baidu"}
    return util.get_url_info(query, ip_url , code = "gbk")



def get_ip_location(ip):
    return util.jsonstrtodict(util.getjson(get_bd_ip_local(ip)))['data'][0]['location']


class test(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            print util.getjson(get_bd_ip_local("220.181.111.86"))
            
if __name__ == "__main__":
    print get_ip_location("220.181.111.86")





    
