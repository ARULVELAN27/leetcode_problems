class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        l=[]
        for x in range(0,len(s)):
            for y in range(x+1,len(s)):
                if s[x]==s[y]:
                    l.append(abs(x-y))
        if len(l)==0:
            return -1
        return max(l)-1
        
