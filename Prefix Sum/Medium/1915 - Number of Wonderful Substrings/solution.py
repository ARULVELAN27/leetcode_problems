class Solution(object):
    def areAlmostEqual(self, s1, s2):
        a=0
        for x in s1:
            if s1.count(x)!=s2.count(x):
                return False
        for x in range(len(s1)):
            if s1[x]!=s2[x]:
                a=a+1
                if s2[x] not in s1:
                    return False
        if a==0 or a==2:
            return True
        return False
        
