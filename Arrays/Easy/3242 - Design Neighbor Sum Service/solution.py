class Solution(object):
    def maxFrequencyElements(self, nums):
        a=0
        l=[]
        for x in nums:
            if nums.count(x)>a:
                a=nums.count(x)
        for y in nums:
            if nums.count(y)==a:
                l.append(y)
        w=len(l)
        return w
        
