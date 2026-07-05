class Solution(object):
    def minimumChairs(self, s):
        a=0
        b=0
        for x in s:
            if x=="E":
                a=a+1
            else:
                a=a-1
            if a>b:
                b=a
        return b
        
