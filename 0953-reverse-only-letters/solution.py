class Solution(object):
    def reverseOnlyLetters(self, s):
        l = []
        i=[]
        h = list(s)
        p = h[:]
        for x in range(len(s)):
            k = s[x]
            if k.isalpha() == False:
                l.append(x)
                i.append(s[x])
                p.remove(s[x])
        p = p[::-1]
        for x in range(len(l)):
            p.insert(l[x], i[x])
        return "".join(p)

        
