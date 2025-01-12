class Solution(object):
    def findClosestNumber(self, nums):
        a=max(nums)
        b=max(nums)
        for x in nums:
            if abs(x)<a or (abs(x)== a and abs(x)>b):
                a=abs(x)
                b=x
        return b

        
