class Solution(object):
    def sumZero(self, n):
        l=[]
        if n%2==0:
            for x in range(1,int((n+2)/2)):
                l.append(x)
                l.append(-1*x)
            return l
        else:
            for x in range(1,int((n+1)/2)):
                l.append(x)
                l.append(-1*x)
            l.append(0)
            return l


        
