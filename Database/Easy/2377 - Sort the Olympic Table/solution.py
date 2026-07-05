class Solution(object):
    def digitCount(self, num):
        l=[]
        for x in range(0,len(num)):
            a=int(num[x])
            l.append(a)
        for y in range(0,len(num)):
            b=l[y]
            c=l.count(y)
            if c!=b:
                return False
        return True

        
