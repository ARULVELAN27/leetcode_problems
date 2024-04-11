class Solution(object):
    def findMaxK(self, nums):
        l=[]
        l1=[]
        for x in nums:
            if x<0:
                l.append(x)
        for y in l:
            if abs(y) in nums:
                l1.append(abs(y))
        if len(l1)==0:
            return -1 
        else:
            return max(l1)     
