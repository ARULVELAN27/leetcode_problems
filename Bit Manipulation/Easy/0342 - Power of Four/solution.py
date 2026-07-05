class Solution(object):
    def isPowerOfFour(self, n):
        for i in range(31):
            ans = pow(4,i)
            if ans == n:
                return True
        return False
        
