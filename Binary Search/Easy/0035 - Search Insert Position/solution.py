class Solution(object):
    def searchInsert(self, nums, target):
        for x in range(0,len(nums)):
            if target<=nums[x]:
                return x
        return len(nums)
