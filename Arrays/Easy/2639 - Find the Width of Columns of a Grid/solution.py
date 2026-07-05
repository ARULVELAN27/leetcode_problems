class Solution(object):
    def separateDigits(self, nums):
        l=[]
        for x in nums:
            for y in str(x):
                l.append(int(y))
        return l
        
