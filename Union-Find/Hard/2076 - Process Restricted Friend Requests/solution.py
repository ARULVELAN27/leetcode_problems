class Solution(object):
    def getLucky(self, s, k):
        a=""
        b=0
        o=0
        for x in s:
            a=a+str(ord(x)-96)
        while b<k:
            b=b+1
            for x in a:
                o=o+int(x)
            a=str(o)
            o=0
        return int(a)
        
