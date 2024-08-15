class Solution(object):
    def maxPower(self, s):
        a=[0]
        b=1
        if len(s)==1:
            return 1
        for x in range(0,len(s)-1):
            if s[x] == s[x+1]:
                b=b+1
            else:
                a.append(b)
                b=1
        a.append(b)
        return max(a)
        
