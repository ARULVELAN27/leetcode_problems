class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        a=0
        for x in range(1,len(arr)+1):
            for y in range(0,len(arr)-x+1):
                if len(arr[y:y+x])%2!=0:
                    a=a+sum(arr[y:y+x])
        return a
        
