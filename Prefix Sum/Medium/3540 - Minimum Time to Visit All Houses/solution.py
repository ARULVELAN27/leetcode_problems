class Solution(object):
    def stringHash(self, s, k):
        o=""
        b=0
        while(len(s)>0):
            a=s[0:k]
            for y in a:
                b=b+ord(y)-97
            o= o+chr((b%26)+97)
            b=0
            s=s[k:len(s)]
        return o
