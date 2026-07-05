class Solution(object):
    def countAsterisks(self, s):
        a=0
        b=0
        for x in s:
            if a==0 and x=="*":
                b=b+1
            elif x=="|":
                a=a+1
                if a==2:
                    a=0

        return b
        
