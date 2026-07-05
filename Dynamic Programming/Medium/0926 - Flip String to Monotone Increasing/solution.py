class Solution(object):
    def findAndReplacePattern(self, words, t):
        l=[]
        for x in words:
            s=x
            e=set()
            for x in range(len(s)):
                e.add((s[x],t[x]))
            if len(e)==len(set(s)) and len(set(s))==len(set(t)):
                l.append(s)
            e.clear()
        return l
