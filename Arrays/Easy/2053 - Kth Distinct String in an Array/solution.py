class Solution(object):
    def areOccurrencesEqual(self, s):
        l=[]
        for x in s:
            l.append(x)
        for y in range(0,1):
            for z in range(1,len(s)):
                if l.count(l[y])!=l.count(l[z]):
                    return False
        return True
        
        
