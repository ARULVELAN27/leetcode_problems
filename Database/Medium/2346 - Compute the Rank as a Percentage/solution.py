class Solution(object):
    def largestGoodInteger(self, nums):
        l=[]
        for x in range(0,len(nums)-2):
            if nums[x]==nums[x+1] and nums[x+1]==nums[x+2]:
                l.append(int(nums[x]))
        if len(l)==0:
            return ""
        return str(max(l))*3
        
        
