class Solution(object):
    def partitionString(self, s):
        i=0
        l=[]
        a=""
        y=set()
        for x in s:
            a=a+x
            if a not in y:
                l.append(a)
                y.add(a)
                a=""
        return l
                
        
