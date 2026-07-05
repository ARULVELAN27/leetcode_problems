class Solution(object):
    def missingNumber(self, nums):
        a=len(nums)
        c=a+1
        q=0
        for i in range(0,c):
            if i in nums:
                q=q+1
                
            else:
                return i


        
