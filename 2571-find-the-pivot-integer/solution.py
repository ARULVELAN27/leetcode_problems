class Solution(object):
    def pivotInteger(self, n):
        for x in range(1,n+1):
            if sum(x for x in range(1,x+1))==sum(x for x in range(x,n+1)):
                return x
        return -1
        
