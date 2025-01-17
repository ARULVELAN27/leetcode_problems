class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        for x in range(k):
            nums[0]=-1*nums[0]
            nums.sort() 
        return sum(nums)
        
