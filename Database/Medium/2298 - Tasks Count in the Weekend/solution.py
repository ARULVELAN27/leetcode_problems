class Solution(object):
    def countEven(self, num):
        l=[]
        a=0
        for x in range(1,num+1):
            for y in str(x):
                a=a+int(y)
            if a%2==0:
                l.append(a)
                a=0
            else:
                a=0
        return len(l)
        
