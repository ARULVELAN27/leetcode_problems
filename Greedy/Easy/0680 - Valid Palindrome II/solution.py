class Solution(object):
    def validPalindrome(self, s):
        s=list(s)
        a=s[::-1]
        p=s[:]
        o=s[:]
        if a==s:
            return True
        for x in range(len(s)):
            if s[x]!=s[len(s)-x-1]:
                p.pop(x)
                o.pop(len(s)-x-1)
                if o==o[::-1] or p==p[::-1]:
                    return True
                return False



                
                

        
