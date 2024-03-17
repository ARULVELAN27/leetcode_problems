class Solution(object):
    def mostFrequentEven(self, nums):
        nums.sort()
        l=[]
        c=0
        for x in nums:
            d=x%2
            if d==0:
                l.append(x)
        if len(l)==0:
            return -1
        else:
            for x in l:
                if l.count(x)>c:
                    c=l.count(x)
                    j=x
                
        return j
