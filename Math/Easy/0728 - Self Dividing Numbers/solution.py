class Solution(object):
    def selfDividingNumbers(self, le, r):
        l=[]
        a=True
        for x in range(le,r+1):
            p=str(x)
            for y in p:
                if y=="0" or x%(int(y))!=0:
                    a=False
                    break
            if a==True:
                l.append(x)
            a=True
        return l
            


