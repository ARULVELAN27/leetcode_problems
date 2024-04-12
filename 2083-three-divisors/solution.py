class Solution(object):
    def isThree(self, n):
        a=0
        for x in range(1,n+1):
            if n%x==0:
                a=a+1
        if a==3:
            return True
        else:
            return False

        
