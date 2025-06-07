class Solution(object):
    def construct2DArray(self, a, m, n):
        l=[]
        e=[]
        if m*n!=len(a):
            return l
        for x in range(m):
            for y in range(n):
                l.append(a[0])
                a.pop(0)
            e=e+[l]
            l=[]
        
        return e
        
