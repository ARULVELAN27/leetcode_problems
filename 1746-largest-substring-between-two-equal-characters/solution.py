class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        d={}
        max1=-1
        for x in range(len(s)):
            if s[x] in d:
                if max1<x-d[s[x]]-1:
                    max1=x-d[s[x]]-1
            else:
                d[s[x]]=x
        return max1



        
