class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        c=0
        v=0
        r=0
        q=0
        w=0
        for i in nums1:
            c=c+1
        for j in nums2:
            v=v+1
        for x in nums2:
             nums1.append(x)
             nums1.sort()
        k=c+v
        o=k/2
        if k%2!=0:
            a = k / 2
            b=round(a)
            b=int(b)
           
            
            r=nums1[b]
            return r
        if k%2 == 0:
            q = k / 2 
            w =( k / 2)-1
            p=nums1[q]+nums1[w]
            p=float(p)
            p=p/2
            
            
            return p


        
