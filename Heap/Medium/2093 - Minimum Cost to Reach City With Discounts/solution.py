class Solution(object):
    def isPrefixString(self, s, words):
        a=""
        for x in words:
            a=a+x
            if s==a:
                return True
        
