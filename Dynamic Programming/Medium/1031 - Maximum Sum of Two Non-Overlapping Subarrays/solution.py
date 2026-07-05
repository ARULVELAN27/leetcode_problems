class Solution(object):
    def addToArrayForm(self, num, k):
        a=""
        l=[]
        for x in num:
            a=a+str(x)
        for y in str(int(a)+k):
            l.append(int(y))
        return l
        
