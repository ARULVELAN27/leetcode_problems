class Solution(object):
    def checkRecord(self, s):
        if "LLL" in s or s.count('A')>=2:
            return False
        else:
            return True
        
        
