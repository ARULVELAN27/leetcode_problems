class Solution(object):
    def cellsInRange(self, s):
        l=[]
        for x in range(ord(s[0]),ord(s[3])+1):
            for y in range(ord(s[1]),ord(s[4])+1):
                l.append(chr(x)+chr(y))
        return l
        
