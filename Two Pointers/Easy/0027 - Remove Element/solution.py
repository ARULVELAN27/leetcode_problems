class Solution(object):
    def removeElement(self, nums, val):
        for x in range(0,5):
            for x in nums:
                if x==val:
                    nums.remove(x)
        return len(nums)        
