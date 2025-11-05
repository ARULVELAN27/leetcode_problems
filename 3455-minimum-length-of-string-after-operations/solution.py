class Solution(object):
    def minimumLength(self, s):
        a=len(s)
        b=""
        c=0
        for x in s:
            if x not in b:
                if s.count(x)>=3:
                    if s.count(x)%2==0:
                        c=c+2
                    else:
                        c=c+1
                    
                else:
                    c=c+s.count(x)
                b=b+x
        return c
        
