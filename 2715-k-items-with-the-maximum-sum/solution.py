class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        l=[]
        a=0
        for x in range(0,numOnes):
            l.append(1)
        for y in range(0,numZeros):
            l.append(0)
        for z in range(0,numNegOnes):
            l.append(-1)
        l.sort(reverse=True)
        for r in range(0,k):
            a=a+l[r]
        return a
        
