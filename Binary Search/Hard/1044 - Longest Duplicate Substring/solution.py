class Solution(object):
    def commonChars(self, words):
        a=set(words[0])
        for x in words[1:len(words)]:
            b=set(x)
            a=a.intersection(b)
        b=list(a)
        u=len(words[0])
        p=[]
        l=[]
        for x in b:
            for y in words:
                if y.count(x)<u:
                    u=y.count(x)
            l=l+([x]*u)
            u = len(words[0])
        return l
        
        
