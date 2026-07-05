class Solution(object):
    def buildArray(self, nums):
        l=[]
        for x in range(0,len(nums)):
            l.append(nums[nums[x]])
        return l
        
