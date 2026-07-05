class Solution(object):
    def countKDifference(self, nums, k):
        a=0
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if abs(nums[x]-nums[y])==k:
                    a=a+1
        return a
        
