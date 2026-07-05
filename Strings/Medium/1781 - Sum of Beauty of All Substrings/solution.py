class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        a=""
        b=""
        for x in word1:
            a=a+x
        for y in word2:
            b=b+y
        if a==b:
            return True
        else:
            return False
        
