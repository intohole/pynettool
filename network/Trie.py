#coding=utf-8
#!/usr/bin/env python




class TrieNode(object):
    
    def __init__(self):
        self.value = -1
        self.children = {}


#词典树 
#功能： 提高查询速度
#方法： 
#    add()
#    search()


class Trie(object):
    
    
    def __init__(self):
        self.root = TrieNode()
    
    
    def add(self , words , value):
        node = self.root
        for word in words.decode("utf-8"):
            if node.children.has_key(word):
                node = node.children[word]
            else:
                t = TrieNode()
                node.children[word] = t
                node = t
        node.value = value
    
    
    def search(self , words):
        node = self.root
        _id = None
        _word = ''
        _add = ''
        for word in words.decode("utf-8"):
            if not node.children.has_key(word):
                break
            else:
                node = node.children[word]
                _add = _add + word
                if node.value > -1:
                    _word = _word + " " + _add
                    _add = ''
                    _id = node.value
        return (_word , _id)
    
if __name__ == "__main__":
    t = Trie()
    t.add("我爱天安门", 1)
    print t.search("他爱")
    
                
        
                
                
            
        
        