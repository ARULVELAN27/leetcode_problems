class Solution(object):
    def check(self, nums):
        a = nums[:]
        a.sort()
        for x in range(len(nums)):
            nums = nums[1:len(nums)] + nums[0:1]
            if nums == a:
                return True
        return False
        
