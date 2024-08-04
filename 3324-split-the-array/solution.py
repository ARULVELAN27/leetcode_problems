class Solution(object):
    def isPossibleToSplit(self, nums):
        for x in nums:
            if nums.count(x)>2:
                return False
        return True
        
