class Solution(object):
    def getCommon(self, nums1, nums2):
        a=set(nums1)
        b=set(nums2)
        c=a.intersection(b)
        b=list(c)
        b.sort()
        if len(b)==0:
            return -1
        return b[0]
        
