class Solution(object):
    def diagonalSum(self, mat):
        a=0
        if len(mat)%2==0:
            for x in range(0,len(mat)):
                a=a+mat[x][x]+mat[x][len(mat)-1-x]
            return a
        else:
            for x in range(0,len(mat)):
                a=a+mat[x][x]+mat[x][len(mat)-1-x]
            a=a-mat[int(len(mat)/2)][int(len(mat)/2)]
            return a

        
