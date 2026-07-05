class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=0
        l=[]
        for x in nums:
            if  x==1:
                a=a+1
                l.append(a)
            else:
                l.append(a)
                a=0
        return max(l)
        
