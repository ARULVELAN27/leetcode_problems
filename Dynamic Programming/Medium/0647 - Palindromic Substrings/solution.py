class Solution(object):
    def countSubstrings(self, s):
        a=0
        for x in range(1,len(s)+1):
            for y in range(len(s)-x+1):
                r=s[y:y+x]
                f=r[::-1]
                if f==r:
                    a=a+1
        return a
        
