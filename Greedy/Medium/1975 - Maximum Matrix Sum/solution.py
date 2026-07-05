class Solution(object):
    def getMinDistance(self, nums, target, start):
        a=max(nums)
        for x in range(start,-1,-1):
            if nums[x]==target and abs(start-x)<a:
                a=abs(start-x)        
        for x in range(start,len(nums)):
            if nums[x]==target and abs(start-x)<a:
                a=abs(start-x)
        return a
                
        
        
