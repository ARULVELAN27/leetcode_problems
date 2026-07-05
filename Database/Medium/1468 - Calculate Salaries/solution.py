class Solution(object):
    def checkIfExist(self, arr):
        for x in arr:
            if x==0:
                arr.remove(0)
        for x in arr:
            if  x*2 in arr:
                return True
        
