class Solution(object):
    def commonFactors(self, a, b):
        l=[]
        l1=[]
        g=0
        for x in range(1,a+1):
            if a%x==0:
                l.append(x)
        for y in range(1,b+1):
            if b%y==0:
                l1.append(y)
        for w in l:
            if w in l1:
                g=g+1
        return g

        
