class Solution(object):
    def minLength(self, s):
        a="AB"
        b="CD"
        while True:    
            if a in s:
                s = s.replace("AB", "", s.count("AB"))
            elif b in s:
                s = s.replace("CD", "", s.count("CD"))
            else:
                break
        return len(s)
