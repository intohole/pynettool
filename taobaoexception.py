#coding=utf-8


class TaoBaoException(Exception):
    
    def __init__(self, reason , code):
        self.reason = reason.encode('utf-8')
        self.errocode = code

    def __str__(self):
        return "%s,%s" % (self.reason,self.errocode)