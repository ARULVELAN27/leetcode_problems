class Solution(object):
    def moveZeroes(self, nums):
        index=0
        for x in range(len(nums)):
            if nums[x]!=0:
                nums[index]=nums[x]
                index+=1
        while index<len(nums):
            nums[index]=0
            index+=1
        return nums
        
