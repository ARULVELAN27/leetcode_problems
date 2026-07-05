class Solution(object):
    def peakIndexInMountainArray(self, arr):
        a=max(arr)
        for x in range(0,len(arr)):
            if arr[x]==a:
                return x
        
