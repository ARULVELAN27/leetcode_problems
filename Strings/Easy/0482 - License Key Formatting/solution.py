class Solution(object):
    def licenseKeyFormatting(self, s, k):
        a=""
        b=""
        c=0
        for x in s:
            if x!="-":
                a=a+x
        a=a.upper()
        a=a[::-1]
        for x in a:
            if c==k:
                b=b+"-"
                c=0
            b=b+x
            c=c+1
            
        return b[::-1]
            


        
