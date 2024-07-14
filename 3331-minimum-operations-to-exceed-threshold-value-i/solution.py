class Solution(object):
    def minOperations(self, nums, k):
        a=0
        for x in nums:
            if x<k:
                a=a+1
        return a
