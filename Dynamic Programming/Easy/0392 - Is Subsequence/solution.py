class Solution(object):
    def isSubsequence(self, s, t):
        a=""
        r=s
        if len(s)>0:
            for x in t:
                if x==s[0]:
                    a=a+x
                    s=s[1:]
                    if len(s)==0:
                        break
            if r==a :
                return True
            return False
        else:
            return True
        
