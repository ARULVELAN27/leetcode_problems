class Solution(object):
    def duplicateNumbersXOR(self, nums):
        num = []
        w=0
        for x in nums:
            if x not in num and nums.count(x)==2:
                num.append(x)
                w=w^x
        return w
