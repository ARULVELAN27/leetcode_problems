class Solution(object):
    def alternateDigitSum(self, n):
        a=0
        for x in range(0,len(str(n))):
            if x%2==0:
                a=a+int(str(n)[x])
            else:
                a=a-int(str(n)[x])
        return a

        
