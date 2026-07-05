class Solution(object):
    def maxSubsequence(self, nums, k):
        y=nums[:]
        nums.sort()
        a=nums[len(nums)-k:len(nums)]    
        p=[]
        for x in y:
            if x in a and a.count(x)!=p.count(x):
                p.append(x)
        return p


        
