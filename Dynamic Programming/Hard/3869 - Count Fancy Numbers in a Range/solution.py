class Solution(object):
    def smallestIndex(self, nums):
        b=0
        for x in range(len(nums)):
            for y in str(nums[x]):
                b=b+int(y)
            if x==b:
                return x
            b=0
        return -1

        
