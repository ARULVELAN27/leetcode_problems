class Solution(object):
    def countNegatives(self, grid):
        a=0
        for x in grid:
            for y in x:
                if y<0:
                    a=a+1
        return a
        
