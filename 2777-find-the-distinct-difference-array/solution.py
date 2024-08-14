class Solution(object):
    def distinctDifferenceArray(self, nums):
        q=[]
        for x in range(0,len(nums)):
            a=len(set(nums[:x+1]))  - len(set(nums[x+1:]))
            q.append(a)
        return q        

        
