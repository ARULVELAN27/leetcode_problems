class Solution(object):
    def countPartitions(self, nums):
        a=0
        for x in range(1,len(nums)):
            if (sum(nums[0:x])-sum(nums[x:len(nums)]))%2==0:
                a=a+1
        return a
        
