class Solution(object):
    def kthDistinct(self, arr, k):
        a=0
        for x in arr:
            if arr.count(x)<2:
                a=a+1
                if a==k:
                    return x
        return ""

