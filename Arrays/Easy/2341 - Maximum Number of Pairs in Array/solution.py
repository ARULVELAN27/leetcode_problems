class Solution(object):
    def countPrefixes(self, words, s):
        a=0
        for x in words:
            if s.startswith(x):
                a=a+1
        return a 
        
