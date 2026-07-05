class Solution(object):
    def isCovered(self, ranges, left, right):
        l = []
        b = list(range(left, right + 1))
        for x in ranges:
            for y in range(x[0],x[1]+1):
                if y in b and len(b)>0:
                    b.remove(y)
        if len(b)>0:
            return False
        return True
        
