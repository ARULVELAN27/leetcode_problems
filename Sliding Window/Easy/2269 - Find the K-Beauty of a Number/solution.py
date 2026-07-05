class Solution(object):
    def countElements(self, nums):
        a=min(nums)
        c=0
        b=max(nums)
        for x in nums:
            if a<x and b>x:
                c=c+1
        return c
        
