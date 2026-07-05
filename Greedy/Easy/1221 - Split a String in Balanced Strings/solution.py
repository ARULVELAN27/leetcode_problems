class Solution(object):
    def findSpecialInteger(self, arr):
        a=float((len(arr)*25)/100)
        b=list(set(arr))
        for x in b:
            if arr.count(x)>a:
                return x
        
