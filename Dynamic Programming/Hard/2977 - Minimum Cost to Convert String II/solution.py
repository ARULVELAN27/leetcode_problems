class Solution(object):
    def isAcronym(self, words, s):
        a=""
        for x in words:
            a=a+x[0]
        if a==s:
            return True
        
        
