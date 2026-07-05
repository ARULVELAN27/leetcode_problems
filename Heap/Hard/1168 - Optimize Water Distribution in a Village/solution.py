class Solution(object):
    def duplicateZeros(self, arr):
        l=[]
        factor=0
        b=len(arr)
              
        for x in range(len(arr)):
            if arr[x]==0:
                l.append(x)
        for y in l:
            arr.insert(factor+y,0)
            factor+=1
        while len(arr)>b:
            arr.pop()
        return arr
                

