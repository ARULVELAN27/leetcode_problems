class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort() 
        l=0
        best=float('inf')
        count=0
        for x in range(len(nums)):
            count+=1
            while count>k:
                l+=1
                count-=1
            if count==k:
                best=min(nums[x]-nums[l],best) 
        return best
