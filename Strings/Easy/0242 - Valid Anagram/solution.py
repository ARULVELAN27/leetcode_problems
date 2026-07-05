class Solution(object):
    def isAnagram(self, s, t):
        a=list(s)
        a.sort()
        b=list(t)
        b.sort()
        if a==b:
            return True
        return False

        
