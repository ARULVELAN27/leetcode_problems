class Solution(object):
    def numOfStrings(self, patterns, word):
        a=0
        for x in patterns:
            if x in word:
                a=a+1
        return a 
        
