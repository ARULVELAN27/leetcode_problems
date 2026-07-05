class Solution(object):
    def makeFancyString(self, s):
        a=""
        for x in range(len(s)):
            if len(a)<2:
                a=a+s[x]
            elif a[-1]!=s[x] or a[-2]!=s[x]:
                a=a+s[x]
        return a
            
                    
