class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k=len(nums1)-1
        for x in range(0,n):
            nums1.pop(k)
            k=k-1
        for y in nums2:
            nums1.append(y)
        nums1.sort()
        return nums1
        
