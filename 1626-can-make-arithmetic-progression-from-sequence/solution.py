class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        a=arr[0]-arr[1]
        for x in range(0,len(arr)-1):
            if arr[x]-arr[x+1]!=a:
                return False
        return True
        
