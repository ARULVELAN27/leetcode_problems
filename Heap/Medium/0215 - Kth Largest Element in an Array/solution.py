class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        g=k-1
        h=nums[g]
        return h
        
        
