class Solution(object):
    def findKthPositive(self, arr, k):
        a=1
        b=1
        while(True):
            if b not in arr and k==a:
                return b
            elif b not in arr:
                a=a+1
            b=b+1


        
