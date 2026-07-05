class Solution(object):
    def digitSum(self, s, k):
        l=[]
        a=0
        b=0
        while(len(s)>k):
            if len(s)%k!=0:
                s=s+("0"*(k-(len(s)%k)))
            for x in s:
                a=a+int(x)
                b=b+1
                if b==k:
                    l.append(str(a))
                    t="".join(l)
                    l=[]
                    l.append(t)
                    a=0
                    b=0
            s="".join(l)
            l=[]
        return s
                

        
