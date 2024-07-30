class Solution(object):
    def canAliceWin(self, nums):
        a=0
        b=0
        for x in nums:
            if x<10:
                a=a+x
            else:
                b=b+x
        if a!=b:
            return True
        return False
            
        
