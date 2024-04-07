class Solution(object):
    def runningSum(self, nums):
        l=[nums[0]]
        for x in range(1,len(nums)):
            l.append(l[x-1]+nums[x])
        return l


        
