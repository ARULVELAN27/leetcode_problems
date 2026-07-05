class Solution(object):
    def findTheDifference(self, s, t):
        s=list(s)
        t=list(t)
        while len(t)>0 or len(s)>0:
            if len(t)>len(s):
                for d in t:
                    if d not in s:
                        return d
                    else:
                        s.remove(d)
                        t.remove(d)
            if len(s)>len(t):
                for x in s:
                    if x not in t:
                        return x
                    else:
                        s.remove(x)
                        t.remove(x)
        
        
        
        
