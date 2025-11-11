class Solution(object):
    def doesAliceWin(self, s):
        a="aeiou"
        c=0
        for x in s:
            if x in a:
                c=c+1
        if c==0 :
            return False
        return True
        
