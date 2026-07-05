class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        count=0
        best=0
        for x in range(len(nums)):
            if nums[x]==0:
                count+=1
            while count>k:
                if nums[l]==0:
                    count-=1
                l+=1
            best=max(best,x-l+1)
        return best
        
