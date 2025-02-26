class Solution(object):
    def isValid(self, s):
        l = []
        for x in s:
            if x == "c" and len(l) >= 2 and l[len(l) - 1] == "b" and l[len(l) - 2] == "a":
                l.pop()
                l.pop()
            else:
                l.append(x)
        if len(l) == 0:
            return True
        return False
        
