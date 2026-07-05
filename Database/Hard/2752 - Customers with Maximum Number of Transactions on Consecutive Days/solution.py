class Solution(object):
    def sumOfMultiples(self, n):
        l=[]
        h=0
        for x in range(0,n+1):
            if x%3==0 or x%5==0 or x%7==0:
                l.append(x)
        for y in l:
            h=h+y
        return h

        
