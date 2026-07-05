class Solution(object):
    def subarraySum(self, nums):
        a=0
        for i in range(len(nums)):
            a=a+(sum(nums[max(0,i-nums[i]): i+1]))
        return a

        
