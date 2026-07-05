class Solution(object):
    def checkString(self, s):
        a=[]
        b=[]
        for x in range(0,len(s)):
            if s[x]=='a':
                a.append(x)
            else:
                b.append(x)
        if len(a)==0 or len(b)==0:
            return True
        else:
            for x in a:
                for y in b:
                    if x>y:
                        return False
        return True     
        
