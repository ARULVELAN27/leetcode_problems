class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        l=[]
        for x in range(nums[0],nums[-1]):
            if x not in nums:
                l.append(x)
        return l
        
