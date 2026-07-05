class Solution(object):
    def findChampion(self, grid):
        a=0
        b=0
        for x in range(0,len(grid)):
            if grid[x].count(1)>a:
                a=grid[x].count(1)
                b=x
        return b
        
