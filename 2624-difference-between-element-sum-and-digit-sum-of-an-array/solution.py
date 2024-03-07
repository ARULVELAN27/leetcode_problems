class Solution(object):
    def differenceOfSum(self, nums):
        a=0
        k=[]
        l=0
        for x in nums:
            a=a+x
        for x in nums:
            j=str(x)
            for x in j:
                f=int(x)
                l=l+f
        p=a-l
        g=abs(p)
        return g
        
