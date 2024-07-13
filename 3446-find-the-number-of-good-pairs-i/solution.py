class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        a=0
        for x in range(0,len(nums1)):
            for y in range(0,len(nums2)):
                if nums1[x]%(nums2[y]*k)==0:
                    a=a+1
        return a
        
