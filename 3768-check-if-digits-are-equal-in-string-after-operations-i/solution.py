class Solution(object):
    def hasSameDigits(self, s):
        p=""
        while(len(s)!=2):
            for x in range(len(s)-1):
                p=p+str((int(s[x])+int(s[x+1]))%10)
            s=p
            p=""
        if s[0]==s[1]:
            return True
        return False


        
