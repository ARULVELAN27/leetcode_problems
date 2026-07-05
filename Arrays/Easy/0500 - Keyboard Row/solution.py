class Solution(object):
    def findWords(self, words):
        a="qwertyuiopQWERTYUIOP"
        b="asdfghjklASDFGHJKL"
        c="zxcvbnmZXCVBNM"
        k=[]
        for x in words:
            l=set()
            for d in x:
                if d in a:
                    l.add(1)
                elif d in b:
                    l.add(2)
                else:
                    l.add(3)
            if len(list(set(l)))==1:
                k.append(x)
        return k
