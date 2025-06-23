class Solution(object):
    def isIsomorphic(self, s, t):
        e=set()
        for x in range(len(s)):
            e.add((s[x],t[x]))
        return len(e)==len(set(s))==len(set(t))
        
