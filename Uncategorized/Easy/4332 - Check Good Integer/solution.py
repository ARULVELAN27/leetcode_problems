class Solution(object):
    def checkGoodInteger(self, n):
        ds=0
        ss=0
        while n>0:
            a=n%10
            ds+=a
            ss+=a*a
            print(a,ds,ss)
            n=n/10

        if ss-ds>=50:
            return True
        return False
        
