class Solution(object):
    def repeatedCharacter(self, s):
        l=[]
        for x in s:
            if x in l:
                return x
            else:
                l.append(x)
        
        
