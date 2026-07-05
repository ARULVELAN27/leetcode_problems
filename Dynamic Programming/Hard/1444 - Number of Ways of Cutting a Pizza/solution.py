class Solution(object):
    def numberOfSteps(self, n):
        a=0
        while n!=0:
            if n%2==0:
                n=n/2
                a=a+1
            else:
                n=n-1
                a=a+1
        return a
        
