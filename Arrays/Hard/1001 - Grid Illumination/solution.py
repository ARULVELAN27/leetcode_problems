class Solution(object):
    def repeatedNTimes(self, nums):
        a=0
        for x in nums:
            if nums.count(x)>a:
                a=nums.count(x)
                b=x
        return b
        
