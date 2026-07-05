class Solution(object):
    def backspaceCompare(self, s, t):
        s=(s.count("#")*"*")+s+(s.count("#")*"*")
        t=(t.count("#")*"*")+t+(t.count("#")*"*")
        b=0
        l=[]
        o=[]
        while b<len(s):
            if s[b]!="#":
                l.append(s[b])
                b=b+1
            else:
                l.pop()
                b=b+1
        l="".join(l)
        l=l.replace("*","")
        b=0
        while b < len(t):
            if t[b] != "#":
                o.append(t[b])
                b = b + 1
            else:
                o.pop()
                b = b + 1
        o="".join(o)
        o=o.replace("*","")
        if l==o:
            return True
        return False
             
    

        
