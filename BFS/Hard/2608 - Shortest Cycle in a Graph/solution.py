class Solution(object):
    def countDigits(self, num):
        a=str(num)
        l=[]
        l2=[]
        p=0
        for x in a:
            s=int(x)
            l.append(s)
            if num%s==0:
                if s not in l2:
                    l2.append(s)
        for d in l2:
            p=p+l.count(d)
        return p
            


        
