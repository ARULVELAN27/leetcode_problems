class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        a={}
        for i,x in enumerate(nums):
            if x in a:
                if i-a[x]<=k:
                    return True
            a[x]=i
        return False
