class Solution(object):
    def scoreOfString(self, s):
        a=0
        for x in range(0,len(s)-1):
            a=a+abs(ord(s[x])-ord(s[x+1]))
        return a
        
