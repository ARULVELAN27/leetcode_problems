class Solution(object):
    def prefixCount(self, words, pref):
        a=0
        for x in words:
            if x.startswith(pref):
                a=a+1
        return a
        
