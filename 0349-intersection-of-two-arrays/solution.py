class Solution(object):
    def intersection(self, nums1, nums2):
        k=[]
        j=[]
        for x in nums1:
            if x in nums2:
                k.append(x)
        for y in k:
            if y not in j:
                j.append(y)
        return j

        
        
