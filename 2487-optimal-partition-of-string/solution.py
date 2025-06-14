class Solution(object):
    def partitionString(self, s):
        a=""
        l=[]
        for x in s:
            if x not in a:
                a=a+x
            else:
                l.append(a)
                a=""
                a=a+x
        l.append(a)
        return len(l)
