class Solution(object):
    def findDifference(self, nums1, nums2):
        l=[]
        l1=[]
        l2=[]
        for x in nums1:
            if x not in nums2:
                if x not in l:
                    l.append(x)
        for y in nums2:
            if y not in nums1:
                if y not in l1:
                    l1.append(y)
        l2.append(l)
        l2.append(l1)
        return l2


       
