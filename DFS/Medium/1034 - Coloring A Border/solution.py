class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.atmost(nums,k)-self.atmost(nums,k-1)
    def atmost(self,nums,k):
        l=0
        d={}
        count=0
        for x in range(len(nums)):
            d[nums[x]]=d.get(nums[x],0)+1
            while len(d)>k:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
            count+=x-l+1
        return count
        
