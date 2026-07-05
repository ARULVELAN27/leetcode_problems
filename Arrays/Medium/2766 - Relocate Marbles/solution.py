class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        a=0
        l=[]
        for x in range(0,len(A)):
            a = len(set(A[:x+1]).intersection(set(B[:x+1])))
            l.append(a)
            a=0
        return l
