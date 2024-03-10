class Solution(object):
    def kthFactor(self, n, k):
        l=[]
        k=k-1
        for x in range(1,n+1):
            if n%x==0:
                l.append(x)
        q=k-1
        if len(l)>k:
            return l[k]
        else:
            return -1
        
