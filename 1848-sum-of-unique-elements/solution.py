class Solution(object):
    def sumOfUnique(self, nums):
        s=0
        for x in nums:
            if nums.count(x)<2:
                s=s+x
        return s
        
        
