class Solution(object):
    def divideArray(self, nums):
        nums.sort()
        for x in range(0,len(nums),2):
            if nums[x]!=nums[x+1]:
                return False
        return True
        
