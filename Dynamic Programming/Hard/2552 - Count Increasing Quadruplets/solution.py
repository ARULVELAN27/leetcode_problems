class Solution(object):
    def maximumSubarraySum(self, nums, k):
        l=0
        d={}
        sum1=0
        best=float('-inf')
        bo=False
        for x in range(len(nums)):
            sum1+=nums[x]
            d[nums[x]]=d.get(nums[x],0)+1
            while d[nums[x]]>1 or x-l+1>k:
                d[nums[l]]-=1
                sum1-=nums[l]
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
            if x-l+1==k:
                best=max(best,sum1)
                bo=True
        if not bo:
            return 0
        return best
