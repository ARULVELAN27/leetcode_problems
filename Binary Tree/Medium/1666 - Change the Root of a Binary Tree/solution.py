class Solution(object):
    def makeGood(self, s):
        l = []
        for x in s:
            if len(l)==0:
                l.append(x)
            elif ord(x)!=ord(l[len(l)-1]) and x.lower()==l[len(l)-1].lower():
                l.pop()
            else:
                l.append(x)
        print(l)
        return "".join(l)
        
