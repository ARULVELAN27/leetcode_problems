class Solution(object):
    def freqAlphabets(self, s):
        s=s[::-1]
        a=""

        while(len(s)!=0):
            if s[0]!="#":
                a=a+chr(96+int(s[0]))
                s=s[1:]
            elif s[0]=="#":
                h=s[1:3]
                h=h[::-1]
                a=a+chr(96+int(h))
                s=s[3:]
        return a[::-1]

        
