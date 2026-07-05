class Solution(object):
    def findPeakElement(self, nums):
        a=max(nums)
        for x in range(0,len(nums)):
            if nums[x]==a:
                return x
        
