class Solution(object):
    def majorityElement(self, nums):
        h=len(nums)/3
        d=int(h)
        l=[]
        s=[]
        for g in range(0,len(nums)):
            k=nums.count(nums[g])
            if k>d:
                l.append(nums[g])
        for t in l:
            if t not in s:
                s.append(t)
        return s

        
