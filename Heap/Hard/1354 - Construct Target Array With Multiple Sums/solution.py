class Solution(object):
    def findWinners(self, matches):
        d = {}
        d[0] = []
        d[1] = []
        for x in matches:
            d[0].append(x[0])
            d[1].append(x[1])
        a = set(d[0])
        b = d[1]
        e = list(a.difference(set(b)))   
        e.sort()
        j = {}
        for n in b:
            j[n] = j.get(n, 0) + 1
        p = [n for n in j if j[n] == 1]
        p.sort()
        return [e, p]

        
        
