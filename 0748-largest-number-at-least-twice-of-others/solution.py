class Solution(object):
    def dominantIndex(self, nums):
        a=max(nums)
        v=nums.index(a)
        nums.remove(a)
    
        for x in nums:
            if 2*x>a:
                return -1
        return v
        
