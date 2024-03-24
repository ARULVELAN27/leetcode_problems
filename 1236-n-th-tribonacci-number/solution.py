class Solution(object):
    def tribonacci(self, n):
        l=[0,1,1]
        a=0
        for x in range(3, n + 1):
            for y in range(x - 1, x - 4,-1):
                a = a + l[y]
            l.append(a)
            a = 0
        e=l[n]
        return e
        
