class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        l=[]
        l1=[]
        l2=[]
        for x in range(0,len(nums1)):
            if nums1[x] in nums2:
                l.append(x)
        for y in range(0,len(nums2)):
            if nums2[y] in nums1:
                l1.append(y)
        if len(l) ==0 or len(l1)==0:
            l2.append(0)
            l2.append(0)
            return l2
        l2.append(len(l))
        l2.append(len(l1))
        return l2
