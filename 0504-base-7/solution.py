class Solution(object):
    def convertToBase7(self, num):
        re=False
        if num==0:
            return "0"
        if num<0:
            num=abs(num)
            re=True
        t=""
        while num>0:
            bit=num%7
            t=str(bit)+t
            num//=7
        if re==True:
            t="-"+t
        return t
        
        
