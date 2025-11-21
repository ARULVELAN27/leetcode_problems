class Solution(object):
    def maxSum(self, nums, m, k):
        d={}
        l=0
        sum1=0
        best=0
        for x in range(len(nums)):
            sum1+=nums[x]
            d[nums[x]]=d.get(nums[x],0)+1
            while x-l+1>k:
                sum1-=nums[l]
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
            if len(d)>=m:
                best=max(best,sum1)
        return best


        
