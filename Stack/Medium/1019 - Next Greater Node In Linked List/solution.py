class Solution(object):
    def sortedSquares(self, nums):
        l=[]
        for x in nums:
            s=x*x
            l.append(s)
        l.sort()
        return l
