class Solution(object):
    def shortestToChar(self, s, c):
        l = [x for x in range(len(s)) if s[x] == c]
        k = []
        for x in range(len(s)):
            p = [abs(x - y) for y in l]
            k.append(min(p))
            p=[]
        return k
