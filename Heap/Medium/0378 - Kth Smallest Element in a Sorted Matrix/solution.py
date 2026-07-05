class Solution(object):
    def kthSmallest(self, matrix, k):
        l=[]
        for x in matrix:
            for y in x:
                l.append(y)
        l.sort()
        i=k-1
        d=l[i]
        return d

        
