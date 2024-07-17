class Solution(object):
    def numberGame(self, nums):
        
        nums.sort()
        for x in range(0,len(nums),2):
            t=nums[x]
            nums[x]=nums[x+1]
            nums[x+1]=t
        return nums
        
