#coding=utf-8



import util


area_url = "http://shangqing.baidu.com/trade/wordPv_view.htm?"


def get_buinese_releate(word):
    query = {'word':word}
    url = util.queryurl(area_url, query)
    return util.get_url_data(url, codemode = "utf-8")


if __name__ == "__main__":
    print get_buinese_releate("三星")