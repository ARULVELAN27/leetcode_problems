class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        a=0
        for e in str(x):
            a=a+int(e)
        if x%a==0:
            return a
        else:
            return -1
        
