class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d=list(magazine)
        for x in ransomNote:
            if x not in d:
                return False
            else:
                d.remove(x)
        return True
        
