class Solution(object):
    def transpose(self, matrix):
        l=[]
        w=[]
        a=0
        for x in range(0,len(matrix[0])):
            for y in range(0,len(matrix)):
                l.append(matrix[a][x])
                a=a+1
            w.append(l)
            l=[]
            a=0
        return w

        
