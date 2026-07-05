class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    l.append(x)
                    l.append(y)
                    return l
        
