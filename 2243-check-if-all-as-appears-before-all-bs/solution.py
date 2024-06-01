class Solution(object):
    def checkString(self, s):
        a=0
        flag=False
        for x in range(0,len(s)):
            if s[x]=="b":
                a=x
                flag=True
                break
        if flag==False:
            return True
        for y in range(a,len(s)):
            if s[y]=="a":
                return False
        return True
        
