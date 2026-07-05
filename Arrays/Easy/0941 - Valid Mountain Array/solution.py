class Solution(object):
    def sortArrayByParity(self, nums):
        l=[]
        for x in nums:
            if x%2==0:
                l.insert(0,x)
            else:
                l.insert(len(l),x)
        return l

        
