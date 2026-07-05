class Solution(object):
    def findMiddleIndex(self, nums):
        for x in range(0,len(nums)):
            a=sum(nums[x+1:])
            b=sum(nums[:x])
            if a==b:
                return x
        return -1
        
