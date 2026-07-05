class Solution(object):
    def averageValue(self, nums):
        l=[]
        a=0
        b=0
        for x in nums:
            if x%3==0 and x%2==0:
                a=a+x  
                b=b+1
        if b==0:
            return 0
        return int(a/b)
        
