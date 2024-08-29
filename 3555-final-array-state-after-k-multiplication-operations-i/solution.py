class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for x in range(0,k):
            a=min(nums)
            for y in range(0,len(nums)):
                if nums[y]==a:
                    nums[y]=nums[y]*multiplier
                    break
        return nums

        
