class Solution(object):
    def removeDuplicates(self, nums):
        for x in nums:
            if nums.count(x)>2:
                nums.remove(x)
        for x in nums:
            if nums.count(x)>2:
                nums.remove(x)
        return len(nums)
