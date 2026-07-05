class Solution(object):
    def matrixReshape(self, mat, r, d):
        a=[]
        b=[]
        c=[]
        
        for x in mat:
            for y in x:
                c.append(y)
        if r*d!=len(c):
            return mat
        for x in range(r):
            for y in range(d):
                a.append(c[0])
                c.remove(c[0])
            b.append(a)
            a=[]
        return b

        
