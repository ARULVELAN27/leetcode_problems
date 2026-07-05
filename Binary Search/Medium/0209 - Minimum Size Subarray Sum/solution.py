class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        sum1=0
        best=len(nums)
        bo=False
        for x in range(len(nums)):
            sum1+=nums[x]
            while sum1>=target:
                best=min(best,x-l+1)
                bo=True
                sum1-=nums[l]
                l+=1
        if not bo:
            return 0
        return best

            
        
