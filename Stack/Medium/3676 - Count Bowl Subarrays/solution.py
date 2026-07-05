class Solution(object):
    def smallestNumber(self, n):
        b="1"
        while True:
            if len(set(list(bin(n)[2:])))==1 and (b in list(bin(n)[2:])):
                break
            n=n+1
        return n
        
