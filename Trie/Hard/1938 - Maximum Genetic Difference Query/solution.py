class Solution(object):
    def minOperations(self, nums):
        a=0
        for x in range(1,len(nums)):
            if nums[x]<=nums[x-1]:
                a+=(nums[x-1]-nums[x]+1)
                nums[x]=nums[x-1]+1
        return a
            


        
