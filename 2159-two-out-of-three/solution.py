class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        a=[]
        for x in nums1:
            if x in nums2 or x in nums3:
                if x not in a:
                    a.append(x)
        for x in nums2:
            if x in nums1 or x in nums3 :
                if x not in a:
                    a.append(x)
        
        return a
        
