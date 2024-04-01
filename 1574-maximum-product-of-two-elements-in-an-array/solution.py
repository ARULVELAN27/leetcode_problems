class Solution(object):
    def maxProduct(self, nums):
        a=max(nums)
        nums.remove(a)
        b=max(nums)-1
        a=a-1
        return a*b

        
