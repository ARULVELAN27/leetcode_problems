class Solution(object):
    def superPow(self, a, b):
        y= int("".join(map(str, b)))
        s=pow(a,y,1337)
        return s
