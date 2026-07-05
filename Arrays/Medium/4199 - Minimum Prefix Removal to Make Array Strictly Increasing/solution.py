class Solution(object):
    def minimumPrefixLength(self, nums):
        nums=nums[::-1]

        for x in range(len(nums)-1):
            if nums[x]<=nums[x+1]:

                return len(nums[x+1:len(nums)])
        return 0
        
