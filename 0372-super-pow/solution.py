class Solution(object):
    def superPow(self, a, b):
        v=len(b)
        if 1 <= a and a <=(pow(2,31)-1):
            if 1 <= v and v <= 2000:
                q = int("".join(map(str, b)))
                t=pow(a,q,1337)
                return t
            else:
                return 0
        else:
            return 0

            
        
        
        
