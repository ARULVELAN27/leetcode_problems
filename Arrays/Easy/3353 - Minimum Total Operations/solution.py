class Solution(object):
    def isSubstringPresent(self, s):
        l=[]
        for x in range(0,len(s)-1):
            l.append(s[x:x+2])
        b=s[::-1]
        for x in l:
            if x in b:
                return True
        return False
