class Solution(object):
    def isValid(self, s):
        l = []
        if len(s)==1:
            return False
        for x in s:
            if len(l)==0:
                l.append(x)
            elif (x == ")" and l[len(l) - 1] == "(") or (x == "}" and l[len(l) - 1] == "{") or (x == "]" and l[len(l) - 1] == "["):
                l.pop()
            else:
                l.append(x)
        if len(l)==0:
            return True
        return False

        
