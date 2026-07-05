class Solution(object):
    def trailingZeroes(self, n):
        w=1
        v=0
        c=[]
        d=0
        for x in range(n,0,-1):
            w=w*x
        q=str(w)
        for d in q[::-1]:
            c.append(d)
        for k in c:
            if k=='0':
                v=v+1
            else:return v
        return v
        
        
        
        
