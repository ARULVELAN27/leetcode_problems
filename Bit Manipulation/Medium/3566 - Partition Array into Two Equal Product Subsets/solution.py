class Solution(object):
    def stringSequence(self, t):
        a=97
        b=""
        l=[]
        i=0
        while b!=t:
            b=b+chr(a+i)
            if t.startswith(b):
                l.append(b)
                i=0
            else:
                l.append(b)
                b=b[:len(b)-1]
                i = i + 1
        return l

        
