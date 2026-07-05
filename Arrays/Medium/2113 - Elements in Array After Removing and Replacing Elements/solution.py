class Solution(object):
    def kthLargestNumber(self, nums, k):
        l=[]
        for x in nums:
            a=int(x)
            l.append(a)
            l.sort(reverse=True)
        if len(l)>=k:
            return str(l[k-1])
        else:
            return str(min(l))
