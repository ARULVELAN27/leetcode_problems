class Solution(object):
    def getSneakyNumbers(self, nums):
        a=[]
        for x in nums:
            if nums.count(x)>1 and x not in a:
                a.append(x)
        return a
        
