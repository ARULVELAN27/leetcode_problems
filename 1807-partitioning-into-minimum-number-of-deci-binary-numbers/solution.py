class Solution(object):
    def minPartitions(self, n):
        a=0
        for x in n:
            if int(x)>a:
                a=int(x)
        return a
