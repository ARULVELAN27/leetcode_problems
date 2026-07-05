class Solution(object):
    def uniqueOccurrences(self, arr):
        l1=[]
        l2=[]
        arr.sort()
        for x in arr:
            if x not in l1:
                l1.append(x)
        for y in l1:
            b=arr.count(y)
            l2.append(b)
        for z in l2:
            w=l2.count(z)
            if w>1:
                return False
        return True
        
