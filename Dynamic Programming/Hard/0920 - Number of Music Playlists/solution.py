class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        r=s1.split(" ")
        t=s2.split(" ")
        a=set(r)
        b=set(t)
        c=list(a.difference(b))
        d=list(b.difference(a))
        e=c[:]
        f=d[:]
        for x in c:
            if r.count(x)!=1:
                e.remove(x)
        for x in d:
            if t.count(x)!=1:
                f.remove(x)
        p=e+f
        return p
