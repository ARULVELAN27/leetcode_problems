class Solution(object):
    def countPairs(self, nums, k):
        a=0
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]==nums[y] and (x*y)%k==0:
                    a=a+1
        return a 
        
