class Solution(object):
    def findLucky(self, arr):
        l=[]
        for x in arr:
            if arr.count(x)==x:
                l.append(x)
        if len(l)>0:
            a=max(l)
            return a
        return -1
        
