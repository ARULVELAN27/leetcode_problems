class Solution(object):
    def appendCharacters(self, s, t):
        c=0
        for x in range(len(t)):
            if t[x] in s:
                s=s[s.index(t[x])+1:]
            else:
                c=c+len(t[x:])
                break
        return c

        
