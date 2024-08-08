class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        s={}
        for x in range(0,len(nums)):
            if nums[x] in s and abs(x-s[nums[x]])<=k:
                return True
            s[nums[x]]=x
        return False
