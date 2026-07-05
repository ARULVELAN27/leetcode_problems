class Solution(object):
    def isPowerOfThree(self, n):
        for i in range(31):
            ans = pow(3,i)
            if ans == n:
                return True
        return False
        
