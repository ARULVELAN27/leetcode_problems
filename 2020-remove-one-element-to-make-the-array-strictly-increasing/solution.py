class Solution(object):
    def canBeIncreasing(self, nums):
        a = nums[:]
        b=False
        if len(nums)==2:
            return True
        for x in range(len(nums)):
            a.pop(x)
            for x in range(len(a)-1):
                if a[x]<a[x+1]:
                    b=True
                else:
                    b=False
                    a=nums[:]
                    break
            if b==True:
                return True
        return False
        
                
    
