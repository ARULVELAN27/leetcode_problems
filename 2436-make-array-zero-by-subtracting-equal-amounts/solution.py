class Solution(object):
    def minimumOperations(self, nums):
        l=[]
        for x in nums:
            if x not in l and x!=0:
                l.append(x)
        return len(l)
        
