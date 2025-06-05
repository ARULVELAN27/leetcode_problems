class Solution(object):
    def minElement(self, nums):
        l=[]
        a=0
        for x in nums:
            for y in str(x):
                a=a+int(y)
            l.append(a)
            a=0
        return min(l)
