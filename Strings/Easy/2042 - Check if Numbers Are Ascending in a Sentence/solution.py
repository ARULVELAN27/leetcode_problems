class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort(reverse=True)
        a=(nums[0]*nums[1])-(nums[len(nums)-1]*nums[len(nums)-2])
        return a

