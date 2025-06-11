class Solution(object):
    def countBits(self, n):
        l=[]
        for x in range(n+1):
            l.append(bin(x)[2:].count("1"))
        return l

        
