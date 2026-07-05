class Solution(object):
    def hasAlternatingBits(self, n):
        a=bin(n)
        a=a[2:len(a)]
        for x in range(len(a)-1):
            if a[x]==a[x+1]:
                return False
        return True
        
