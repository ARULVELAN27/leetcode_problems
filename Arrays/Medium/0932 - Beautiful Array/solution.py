class Solution(object):
    def isMonotonic(self, nums):
        a=nums[:]
        a.sort()
        b=nums[:]
        b.sort(reverse=True)
        if nums == a or nums== b:
            return True
        return False
        
