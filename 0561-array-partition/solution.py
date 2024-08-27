class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        a=sum(nums[0::2])
        return a
        
