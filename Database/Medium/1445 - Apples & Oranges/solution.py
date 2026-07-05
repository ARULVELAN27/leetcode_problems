class Solution(object):
    def numOfSubarrays(self, arr, k, t):
        sum1=0
        count=0
        l=0
        best=0
        for x in arr:
            sum1+=x
            count+=1
            while count>k:
                sum1-=arr[l]
                l+=1
                count-=1
            if sum1//k>=t and count==k:
                best+=1
        return best
        
