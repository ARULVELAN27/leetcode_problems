class Solution(object):
    def findPeaks(self, mountain):
        l=[]
        for x in range(1,len(mountain)-1):
            if mountain[x-1]<mountain[x] and mountain[x]>mountain[x+1]:
                l.append(x)
        return l
        
