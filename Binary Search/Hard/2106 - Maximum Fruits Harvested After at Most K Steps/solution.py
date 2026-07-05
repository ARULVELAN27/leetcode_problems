class Solution(object):
    def findGCD(self, nums):
        a=min(nums)
        b=max(nums)
        l=[]
        for x in range(1,max(nums)+1):
            if a%x==0 and b%x==0:
                l.append(x)
        return max(l)

        
