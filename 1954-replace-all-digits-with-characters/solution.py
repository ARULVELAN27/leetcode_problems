class Solution(object):
    def replaceDigits(self, s):
        a=""
        for x in range(len(s)):
            if s[x].isnumeric()==True:
                a=a+chr(ord(s[x-1])+int(s[x]))
            else:
                a=a+s[x]
        return a
                
        
