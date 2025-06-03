class Solution(object):
    def sortByBits(self, arr):
        for x in range(0,len(arr)):
            for y in range(0,len(arr)-1):
                if bin(arr[y])[2:].count("1")>bin(arr[y+1])[2:].count("1"):
                    temp=arr[y]
                    arr[y]=arr[y+1]
                    arr[y+1]=temp
                elif bin(arr[y])[2:].count("1")==bin(arr[y+1])[2:].count("1") and arr[y]>arr[y+1]:
                    temp=arr[y]
                    arr[y]=arr[y+1]
                    arr[y+1]=temp
        return arr
