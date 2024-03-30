class Solution(object):
    def thirdMax(self, nums):
        l=[]
        nums.sort(reverse=True)
        
        for x in nums:
            if x not in l:
                l.append(x)
        a=len(l)
        if a>=3:
            return l[2]
        else:
            return max(l)

        
