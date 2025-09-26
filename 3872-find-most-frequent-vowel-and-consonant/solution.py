class Solution(object):
    def maxFreqSum(self, s):
        b=s
        p="aeiou"
        con=0
        vov=0
        a=list(set(list(s)))
        for x in a:
            if x in p:
                if b.count(x)>vov:
                    vov=b.count(x)
            else:
                if b.count(x)>con:
                    con=b.count(x)
        return vov+con

        
