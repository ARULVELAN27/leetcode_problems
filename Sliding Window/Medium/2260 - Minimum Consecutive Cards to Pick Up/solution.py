class Solution(object):
    def divideString(self, s, k, fill):
        a=[]
        p=""
        for x in range(0,len(s)):
            if len(p)==k:
                a.append(p)
                p=""
                p=p+s[x]
            else:
                p=p+s[x]
        if len(p)!=0:
            p=p+(fill*(k-len(p)))
            a.append(p)
        return a        
        
