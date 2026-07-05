class Solution(object):
    def clumsy(self, n):
        a=["*" ,"/","+","-"]
        b=0
        l=""
        for x in range(n,0,-1):
            if b==4:
                b=0
            l=l+str(x)+a[b]
            b=b+1
        l=l[0:len(l)-1]
        return eval(l)
            
        
