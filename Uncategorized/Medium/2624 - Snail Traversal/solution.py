class Solution(object):
    def differenceOfSum(self, nums):
        a=0
        for x in nums:
            a=a+x
        b=0
        for y in nums:
            w=str(y)
            for r in w:
                b=b+int(r)
        return abs(a-b)
        
