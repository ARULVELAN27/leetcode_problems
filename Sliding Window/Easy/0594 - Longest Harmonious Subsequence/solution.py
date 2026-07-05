class Solution(object):
    def findLHS(self, nums):
 
        nums.sort()
        l=0
        best=0
        for x in range(len(nums)):
            while nums[x]-nums[l]>1:
                l+=1
            if nums[x]-nums[l]==1:
                best=max(best,x-l+1)
        return best
        


