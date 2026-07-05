class Solution(object):
    def getSum(self, a, b):
        if a > 0 and b>0:
            for x in range(0, b):
                a = a + 1
            return a
        if a>0 and b<0:
            for e in range(b,0):
                a=a-1
            return a
        if a<0 and b>0:
            for e in range(0,b):
                a=a+1
            return a
        if a==0 or b==0:
            if a==0:
                return b
            if b==0:
                return a
        if a<0 and b<0:
            k=abs(b)
            for x in range(0,k):
                a=a-1
            return a
        else:
            return 0
        
