class Solution(object):
    def addSpaces(self, s, s1):
        s1=set(s1)
        a=[]
        for x,ch in enumerate(s):
            if x in s1:
                a.append(" ")
            a.append(ch)
        return "".join(a)

        
