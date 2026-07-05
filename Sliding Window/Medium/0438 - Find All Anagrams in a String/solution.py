class Solution(object):
    def findAnagrams(self, s, p1):
        a = {}  
        d = {} 
        p = []  
        l = 0    
        for x in p1:
            a[x] = a.get(x, 0) + 1
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            while d and d.get(s[l], 0) > a.get(s[l], 0):
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            if d == a:
                p.append(l)

        return p

