class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        a=0
        for x in word1:
            a=abs(word1.count(x)-word2.count(x))
            if a>3:
                return False
        for x in word2:
            a=abs(word1.count(x)-word2.count(x))
            if a>3:
                return False
        return True
        
