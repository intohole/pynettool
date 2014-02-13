# coding=utf-8
#!/usr/bin/env python

import util
import network


SIGN = 'a6a278febdea8e56e53f6bdd6545a399'
URL_FIND = 'http://domaincheck.cndns.com/domaincheck.asp?'


def find_url(word, domias=['com', 'cn']):
    headers = {
        "Host": "domaincheck.cndns.com",
        "Referer": "http://www.cndns.com/cn/domain/full-dme-form.asp"
    }
    query = {
        "id": "",
        "checkdme": "",
        "ttl": "7",
        "sign": SIGN,
        "isname": "",
        "callback": "jQuery17208940748884342611_1383974248620",
        "_": util.timems()
    }
    _ret_count = 1
    for domain in domias:
        query["id"] = 'ret%s' % _ret_count
        query["checkdme"] = '%s.%s' % (word, domias)
        print network.get_html_string(URL_FIND, query, headers)


if __name__ == '__main__':
    find_url('baidu')
