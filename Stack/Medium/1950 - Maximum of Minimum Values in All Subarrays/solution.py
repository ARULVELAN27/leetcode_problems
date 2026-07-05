class Solution(object):
    def arraySign(self, nums):
        a=1
        for x in nums:
            a=a*x  
        if a<0:
            return -1
        elif a>0:
            return 1
        else:
            return 0      
