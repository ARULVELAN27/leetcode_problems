class Solution(object):
    def dividePlayers(self, s):
        s.sort()
        d={}
        a=len(s)
        for x in range(a//2):
            l=[s[x],s[a-x-1]]
            if len(d)==0:
                d[s[x]+s[a-x-1]]=s[x]*s[a-x-1]
            elif s[x]+s[a-x-1] not in d:
                return -1
            else:
                d[s[x]+s[a-x-1]]=d[s[x]+s[a-x-1]]+s[x]*s[a-x-1]
        a=list(d.values())
        return a[0]
        
