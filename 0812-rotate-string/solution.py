class Solution(object):
    def rotateString(self, s, goal):
        if s==goal:
            return True
        for x in range(len(s)-1):
            s = s[1:len(s)] + s[0]
            if s==goal:
                return True
        return False
