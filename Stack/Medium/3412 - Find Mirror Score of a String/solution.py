class Solution(object):
    def findPermutationDifference(self, s, t):
        a=0
        for x in s:
            a=a+(abs(s.index(x)-t.index(x)))
        return a

        
