class Solution(object):
    def numOfPairs(self, nums, target):
        a=0
        for x in range(0,len(nums)):
            for y in range(0,len(nums)):
                if x!=y and nums[x]+nums[y]==target:
                    a+=1
        return a
        
