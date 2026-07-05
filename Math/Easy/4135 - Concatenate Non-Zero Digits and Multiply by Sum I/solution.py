class Solution(object):
    def sumAndMultiply(self, n):
        a=""
        sum1=0
        if n==0:
            return 0
        for x in str(n):
            if x!="0":
                a=a+x
                sum1+=int(x)
        return int(a)*sum1
        
