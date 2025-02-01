class Solution(object):
    def countGoodSubstrings(self, s):
        a=0
        for x in range(len(s)-2):
            p=s[x]+s[x+1]+s[x+2]
            if len(set(p))==3:
                a=a+1
        return a

            
        
