class Solution(object):
    def trimMean(self, arr):
        a=0.05*len(arr)
        arr.sort()
        for x in range(int(a)):
            arr.remove(max(arr))
            arr.remove(min(arr))
        return (float(sum((arr))))/len(arr)
        
