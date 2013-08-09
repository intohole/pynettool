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


    
if __name__ == "__main__":
    print get_search_num("三星")