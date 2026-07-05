class Solution(object):
    def minChanges(self, s):
        a=0
        for x in range(0,len(s),2):
            if len(set(s[x:x+2]))!=1:
                a=a+1
        return a
        
