class Solution(object):
    def singleNumber(self, nums):
        a=0
        while len(nums)>0:
            if nums.count(nums[a])==1:
                return nums[a]
            else:
                a=a+1
        
