class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        l=[]
        for x in range(0,len(arr)-2):
            if arr[x]-arr[x+1]!=arr[x+1]-arr[x+2]:
                return False
        return True
