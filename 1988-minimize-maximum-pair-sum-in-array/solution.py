class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        a=0
        b=len(nums)-1
        ma=0
        while a<b:
            ma=max(ma,nums[a]+nums[b])
            a=a+1
            b=b-1
        return ma

        
