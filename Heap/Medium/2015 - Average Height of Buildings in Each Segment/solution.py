class Solution(object):
    def findRotation(self, mat, target):
        p=len(mat[0])
        for x in range(p*p):
            l = []
            transpose = [[row[i] for row in mat] for i in range(len(mat[0]))]
            for x in transpose:
                p = x[::-1]
                l.append(p)
                p = []
            if l==target:
                return True
            else:
                mat=l
                l=[]
        return False


        
