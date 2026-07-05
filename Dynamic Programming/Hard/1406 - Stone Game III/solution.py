class Solution(object):
    def subtractProductAndSum(self, n):
        a=str(n)
        l=[]
        b=1
        c=0
        for x in a:
            l.append(x)
        for y in l:
            e=int(y)
            b=b*e
        for k in l:
            u=int(k)
            c=c+u
        p=b-c
        return p
        
