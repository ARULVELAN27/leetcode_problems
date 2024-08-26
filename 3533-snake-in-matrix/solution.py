class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        a=[0,0]
        for x in commands:
            if x=="UP":
                a[0]=a[0]-1
            if x=="DOWN":
                a[0]=a[0]+1
            if x=="RIGHT":
                a[1]=a[1]+1
            if x=="LEFT":
                a[1]=a[1]-1
        b=(a[0]*n)+a[1]
        return b
        
