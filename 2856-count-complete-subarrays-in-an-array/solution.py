class Solution(object):
    def countCompleteSubarrays(self, nums):
        k=len(set(nums))
        d={}
        l=0
        count=0
        for x in range(len(nums)):
            d[nums[x]]=d.get(nums[x],0)+1
            while len(d)==k:
                count+=len(nums)-x
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
        return count
        
