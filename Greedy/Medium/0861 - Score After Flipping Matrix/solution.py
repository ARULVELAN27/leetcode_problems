class Solution(object):
    def flipAndInvertImage(self, a):
        for x in range(len(a)):
            b = a[x]
            a[x] = b[::-1]
        for x in range(len(a)):
            for y in range(len(a[0])):
                if a[x][y]==0:
                    a[x][y]=1
                else:
                    a[x][y] = 0
        return a


        
