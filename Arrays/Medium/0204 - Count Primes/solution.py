class Solution(object):
    def countPrimes(self, n):
        if n<2:
            return 0
        l=[True]*n
        l[0]=l[1]=False
        for x in range(2,int(n**0.5)+1):
            if l[x]:
                for j in range(x*x,n,x):
                    l[j]=False
        return sum(l) 
        
