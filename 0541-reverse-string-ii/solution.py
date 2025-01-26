class Solution(object):
    def reverseStr(self, s, k):
        b = 0
        p = ""
        for x in range(0, len(s), k):
            a = s[x:x + k]
            if b % 2 == 0:
                a = a[::-1]
                p = p + a
                b=b+1
            else:
                p = p + a
                b = b + 1
        return p
                


        
