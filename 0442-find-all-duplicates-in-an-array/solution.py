class Solution(object):
    def findDuplicates(self, nums):
        a=[]
        nums.sort()
        for x in range(0,len(nums)-1):
            if nums[x]==nums[x+1]:
                a.append(nums[x])
        return a

