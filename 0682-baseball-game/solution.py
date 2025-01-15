class Solution(object):
    def calPoints(self, operations):
        l=[]
        for x in operations:
            if x=="C":
                l.pop()
            elif x=="D":
                l.append(2*l[len(l)-1])
            elif x=="+":
                l.append(l[len(l)-1]+l[len(l)-2])
            else:
                l.append(int(x))
        return sum(l)
