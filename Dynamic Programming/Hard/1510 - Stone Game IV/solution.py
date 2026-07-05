class Solution(object):
    def findLucky(self, arr):
        a=-1
        for x in arr:
            if arr.count(x)==x and x>a:
                a=x
        return a
        
