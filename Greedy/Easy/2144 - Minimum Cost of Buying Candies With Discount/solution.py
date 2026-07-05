class Solution(object):
    def maximumDifference(self, nums):
        a=-1
        for x in range(len(nums)-1):
            for y in range(x+1,len(nums)):
                e=max(nums[y:len(nums)])
                if nums[x]<e and (e-nums[x])>a:
                    a=e-nums[x]
        return a



        
