# coding=utf-8



import threading
import util
import re


ipregx = re.compile("[0-9]{1,3}(\.[0-9]{1,3}){3}",re.UNICODE)

suggesturl = 'http://esug.baidu.com/su?'
ip_url = "http://opendata.baidu.com/api.php?"
ip_sina_url = "http://counter.sina.com.cn/ip?"

sina_regx = re.compile("Array\([^)]*\)")
 
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
            "t":util.timems(),
            "ie":"utf8",
            "oe":"gbk",
            "cb":"bd__cbs__yk2g9h",
            "format":"json",
            "tn":"baidu"}
    
    return util.get_url_html_string(query, ip_url , code = "gbk")



def get_ip_location(ip):
    return util.jsonstrtodict(util.getjson(get_bd_ip_local(ip)))['data'][0]['location']

def get_sina_ip_info(ip):
    query = {
             "ip":ip,
             "t":util.timems()
             }
    return util.get_url_html_string(query , ip_sina_url,code="gb2312")

def is_ip(ip):
    if ipregx.match(str(ip).strip()):
        return True
    return False

def get_sina_ip_location(ip):
    if not is_ip(ip):
        return "not ip!"         
    data = get_sina_ip_info(ip)
    m = sina_regx.search(data)
    if m:
        location = m.group().split("\"")
        try:
            locationstr = "%s %s %s %s" % (location[3],location[5],location[7],location[9])
        except Exception,e:
            return ""
        return locationstr
    return "not find ip info"
        
    
    

class test(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            print util.getjson(get_bd_ip_local("220.181.111.86"))
            
if __name__ == "__main__":
    print get_bd_ip_local("218.2.129.53")





    
