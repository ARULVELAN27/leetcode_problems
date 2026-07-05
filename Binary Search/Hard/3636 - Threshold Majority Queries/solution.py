class Solution(object):
    def isBalanced(self, num):
        a=[int(x) for x in num[0:len(num):2]]
        b=[int(x) for x in num[1:len(num):2]]
        if sum(a)==sum(b):
            return True
        return False
