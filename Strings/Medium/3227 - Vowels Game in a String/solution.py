class Solution:
    def findMissingAndRepeatedValues(self, grid):
        l=[]
        l1=[]
        for x in grid:
            for y in x:
                l.append(y)
        for d in range(0,len(l)):
            for e in range(d+1,len(l)):
                if l[d]==l[e]:
                    l1.append(l[d])

        b = pow(len(grid),2)
        for x in range(1,b+1):
            if x not in l:
                l1.append(x)
        return l1
                
