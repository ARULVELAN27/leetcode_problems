class Solution(object):
    def findNonMinOrMax(self, nums):
        a=max(nums)
        b=min(nums)
        for x in nums:
            if x!=a and x!=b:
                return x
        return -1
        
