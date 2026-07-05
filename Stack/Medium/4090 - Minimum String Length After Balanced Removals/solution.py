class Solution(object):
    def minLengthAfterRemovals(self, s):
        d={}
        for x in s:
           d[x]=d.get(x,0)+1
        n=len(s)
        f=max(d.values())
        if f>n-f:
            return 2*f-n
        else:
            return 0

