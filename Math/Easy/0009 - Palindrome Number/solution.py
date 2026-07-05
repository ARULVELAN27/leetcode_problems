class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        if a[::-1]==a:
            return True
        return False
        
