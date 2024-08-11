class Solution(object):
    def applyOperations(self, nums):
        for x in range(0,len(nums)-1):
            if nums[x]==nums[x+1]:
                nums[x]=nums[x]*2
                nums[x+1]=0
        l=[]
        for x in range(len(nums)-1,-1,-1):
            if nums[x]==0:
                l.append(0)
            else:
                l.insert(0,nums[x])
        print(l)
        return l
        
