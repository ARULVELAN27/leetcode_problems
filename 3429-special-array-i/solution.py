class Solution(object):
    def isArraySpecial(self, nums):
        for x in range(0,len(nums)-1):
            if nums[x]%2==nums[x+1]%2:
                return False
        return True
        
