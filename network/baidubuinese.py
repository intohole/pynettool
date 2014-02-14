# coding=utf-8


from utils import network


releate_url = "http://shangqing.baidu.com/trade/wordPv_view.htm?" # 相关搜索 地址
search_num_url = "http://shangqing.baidu.com/trade/wordPv_statistics.htm?" #搜索数量 地址
area_url = "http://shangqing.baidu.com/recomword/recomWordCache_findProvPvCache.htm?" # 区域搜索网址




def get_buinese_releate(word):
    query = {'word': word}
    return network.get_html_string(releate_url, query)


def get_search_num(word):
    query = {"word": word}
    return network.get_html_string(search_num_url, query)

def get_area_info(word, num, areaid=''):
    query = {"word": word,
             "num": num,
             "area_id": areaid}
    return network.get_html_string(area_url	, query)


if __name__ == "__main__":
    print get_buinese_releate("三星"  )
    print get_search_num('三星')
    print get_area_info('三星' , 10 )
