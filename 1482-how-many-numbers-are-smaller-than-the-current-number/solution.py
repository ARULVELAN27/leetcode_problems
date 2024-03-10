class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l=[]
        p=0
        for x in nums:
            for y in nums:
                if x>y:
                    p=p+1
            l.append(p)
            p=0
        return l

        
