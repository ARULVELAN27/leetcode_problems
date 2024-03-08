class Solution(object):
    def fib(self, n):
        l=[0,1]
        for x in range(0,n):
            a=l[x]+l[x+1]
            l.append(a)
        p=l[n]
        
        return p
        
        
