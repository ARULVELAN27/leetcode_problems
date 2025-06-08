class Solution(object):
    def sortVowels(self, s):
        l=[]
        t=""
        p="aeiouAEIOU"
        for x in s:
            if x in p:
                l.append(x)
        l.sort()
        for x in s:
            if x in p:
                t=t+l[0]
                l.pop(0)
            else:
                t=t+x
        return t
        
