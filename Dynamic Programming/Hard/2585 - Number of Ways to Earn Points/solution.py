class Solution(object):
    def deleteGreatestValue(self, grid):
        l=[]
        a=0
        for z in range(0,len(grid[0])):
            for x in grid:
                l.append(max(x))
                x.remove(max(x))
            a=a+max(l)
            l=[]
        return a
