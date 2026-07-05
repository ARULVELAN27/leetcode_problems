class Solution(object):
    def countDistinctIntegers(self, nums):
        l=[]
        for x in nums:
            l.append(int(str(x)[::-1]))
        nums=set(nums+l)
        return len(nums)
        
