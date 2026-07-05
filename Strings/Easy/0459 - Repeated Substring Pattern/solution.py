class Solution(object):
    def repeatedSubstringPattern(self, s):
        a=s
        e=""
        for x in range(len(s)-1):
            e=e+s[x]
            a=a.replace(e,"")
            if len(a)==0:
                return True
            else:
                a=s
        return False

        
