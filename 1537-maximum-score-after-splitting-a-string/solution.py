class Solution(object):
    def maxScore(self, s):
        l = []
        a = []
        b = []
        for x in range(0, len(s)-1):
            a = str(s[0:x + 1])
            b = str(s[x+1:len(s)])
            l.append(a.count("0") + b.count("1"))
            a = []
            b = []
        return max(l)
        
