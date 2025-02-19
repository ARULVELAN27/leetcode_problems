class Solution(object):
    def addBinary(self, a, b):
        a=int(a,2)
        b=int(b,2)
        c=bin(a+b)
        return c[2:len(c)]
        
