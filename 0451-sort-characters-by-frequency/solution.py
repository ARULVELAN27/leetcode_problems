class Solution(object):
    def frequencySort(self, s):
        q=[]
        w=[]
        for x in s:
            if x not in q:
                q.append(x)
                w.append(s.count(x))
        p=""
        for x in range(0,len(w)):
            p = p + q[w.index(max(w))] * max(w)
            q.remove(q[w.index(max(w))])
            w.remove(max(w))
        return p
