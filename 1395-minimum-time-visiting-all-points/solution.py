class Solution(object):
    def minTimeToVisitAllPoints(self, q):
        a=0
        for x in range(len(q)-1):
            a=a+max(abs(q[x+1][0]-q[x][0]),abs(q[x+1][1]-q[x][1]))
        return a
