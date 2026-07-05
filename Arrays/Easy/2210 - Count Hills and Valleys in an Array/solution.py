class Solution(object):
    def targetIndices(self, nums, target):
        l=[]
        nums.sort()
        for x in range(0,len(nums)):
            w=nums[x]
            if w==target:
                l.append(x)
        return l
       
        
