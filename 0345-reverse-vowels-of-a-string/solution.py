class Solution(object):
    def reverseVowels(self, s):
        v="aeiouAEIOU"
        l=[]
        p=[]
        for x in s:
            l.append(x)
        for y in range(0,len(s)):
            if s[y] in v:
                p.append(y)
        if len(p)>1:
            for x in range(0,len(p)/2):
                t = l[p[x]]
                l[p[x]] = l[p[len(p) - x-1]]
                l[p[len(p) - x-1]] = t
        q="".join(l)
        return q
        
