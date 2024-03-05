class Solution(object):
    def differenceOfSums(self, n, m):
        l1=[]
        l2=[]
        l3=[]
        for x in range(1,n+1):
            l1.append(x)
        for y in l1:
            if y%m==0:
                l2.append(y)
            else:
                l3.append(y)
        w=sum(l2)
        e=sum(l3)
        p=e-w
        return p
                
        
