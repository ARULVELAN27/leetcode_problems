class Solution(object):
    def checkDivisibility(self, n):
        n=str(n)
        sum=0
        prod=1
        for x in n:
            sum=sum+int(x)
            prod=prod*int(x)
        if int(n)%(sum+prod)==0:
            return True
        return False
