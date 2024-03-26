class Solution(object):
    def maximumCount(self, nums):
        a=0
        b=0
        for y in nums:
            if y<0:
                a=a+1
            elif y>0:
                b=b+1
        if a>b:
            return a
        else:
            return b
        
        
