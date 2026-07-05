class Solution(object):
    def minimumRightShifts(self, nums):
        a = 0
        s = nums[:]
        s.sort()
        for x in range(len(nums)):
            if nums==s:
                return a
            nums= nums[len(nums) - 1:len(nums)] + nums[0:len(nums) - 1]
            a=a+1
        return -1

        
