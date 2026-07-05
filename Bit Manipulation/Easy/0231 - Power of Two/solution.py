class Solution(object):
    def isPowerOfTwo(self, n):
        for i in range(31):
            ans = pow(2,i)
            if ans == n:
                return True
        return False
