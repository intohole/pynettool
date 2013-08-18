#coding=utf-8



import util


releate_url = "http://shangqing.baidu.com/trade/wordPv_view.htm?"
search_num_url = "http://shangqing.baidu.com/trade/wordPv_statistics.htm?"
area_url = "http://shangqing.baidu.com/recomword/recomWordCache_findProvPvCache.htm?"

def get_buinese_releate(word):
    query = {'word':word}
    return util.get_url_info(query, releate_url, "utf-8")


def get_search_num(word):
    query = {"word":word}
    return util.get_url_info(query, search_num_url, "utf-8")

def get_area_info(word,num,areaid=''):
    query = {"word":word,
             "num":num,
             "area_id":areaid}
    return util.get_url_info(query, area_url, code="utf-8")


    
if __name__ == "__main__":
    print get_area_info("三星",30,1)
