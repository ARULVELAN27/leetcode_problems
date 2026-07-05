class Solution(object):
    def minimizedStringLength(self, s):
        a=0
        l=[]
        for x in s:
            if x not in l:
                l.append(x)
                a=a+1
        return a
        
