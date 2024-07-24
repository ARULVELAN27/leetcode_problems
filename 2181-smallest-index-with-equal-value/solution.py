class Solution(object):
    def smallestEqual(self, nums):
        for x in range(0,len(nums)) :
            if x%10==nums[x]:
                return x
                break
        return -1
        
