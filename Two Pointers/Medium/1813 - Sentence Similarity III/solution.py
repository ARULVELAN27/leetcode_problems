class Solution(object):
    def maximumUniqueSubarray(self, nums):
        a=len(set(nums))
        l=0
        d={}
        count=0
        sum1=0
        for x in range(len(nums)):
            sum1+=nums[x]
            d[nums[x]]=d.get(nums[x],0)+1
            while d[nums[x]]>1:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                sum1-=nums[l]
                l+=1
            count=max(count,sum1)
        return count
