class Solution(object):
    def generateTheString(self, n):
        a=""
        if n%2!=0:
            return ('a'*n)
        else:
            return ('a'*(n-1)+'b')
            

        
