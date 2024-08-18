class Solution(object):
    def returnToBoundaryCount(self, nums):
        a=0
        b=0
        for x in nums:
            a=a+x
            if a==0:
                b=b+1
        return b
        
