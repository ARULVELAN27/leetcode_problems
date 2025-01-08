class Solution(object):
    def smallestNumber(self, num):
        l=[]
        num=str(num)
        if num[0]=="-":
            for x in num[1:]:
                l.append(x)
            l.sort(reverse=True)
            b="".join(l)
            return int(-1*int(b))
        else:
            for x in num:
                l.append(int(x))
            a=l.count(0)
            for x in range(a):
                l.remove(0)
            l.sort()
            for x in range(a):
                l.insert(1,0)
            p=[]
            for x in l:
                p.append(str(x))
            return int("".join(p))
        
