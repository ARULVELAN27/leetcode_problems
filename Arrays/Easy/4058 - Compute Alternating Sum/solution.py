class Solution(object):
    def alternatingSum(self, nums):
        a=0
        for x in range(len(nums)):
            if x%2==0:
                a=a+nums[x]
            else:
                a=a-nums[x]
        return a
        
