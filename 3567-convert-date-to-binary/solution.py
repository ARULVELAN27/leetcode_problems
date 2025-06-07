class Solution(object):
    def convertDateToBinary(self, date):
        a=date.split("-")
        t=""
        for x in a:
            b=bin(int(x))[2:]
            t=t+str(b)+"-"
        return t[:len(t)-1]
        
