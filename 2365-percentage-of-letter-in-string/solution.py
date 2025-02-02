class Solution(object):
    def percentageLetter(self, s, letter):
        s=list(s)
        a=s.count(letter)
        b=len(s)
        c=a*100
        c=c/b
        print(c)
        return int(c)        
