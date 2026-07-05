class Solution(object):
    def isPerfectSquare(self, num):
        ans=num**0.5
        if int(ans)==ans:
            return True
        else:
            return False  
        
