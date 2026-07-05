class Solution(object):
    def sumOfSquares(self, nums):
        a=0
        for x in range(1,len(nums)+1):
            if len(nums)%x==0:
                a=a+(nums[x-1]*nums[x-1])
        return a
        
