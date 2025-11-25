class Solution(object):
    def longestSubarray(self, nums):
        l=0
        c0=0
        best=0
        d={}
        for x in range(len(nums)):
            d[nums[x]]=d.get(nums[x],0)+1
            if nums[x]==0:
                c0+=1
            while c0>1:
                if nums[l]==0:
                    c0-=1
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
            best=max(best,x-l)
        return best

