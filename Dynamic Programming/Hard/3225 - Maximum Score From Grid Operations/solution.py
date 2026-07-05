class Solution(object):
    def maxSubarrayLength(self, nums, k):
        index = 0
        d = {}
        count = 0
        max1 = 0
        for x in nums:
            d[x] = d.get(x, 0) + 1
            count += 1
            while d[x] > k:
                d[nums[index]]-= 1
                index += 1
                count -= 1
            max1 = max(max1, count)
        return max1

        
