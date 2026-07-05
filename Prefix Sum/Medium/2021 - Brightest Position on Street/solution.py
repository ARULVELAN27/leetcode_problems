class Solution(object):
    def removeOccurrences(self, s, part):
        l = ""
        for x in range(len(s)):
            if part in l:
                l=l.replace(part, "")
            l=l+s[x]
        if part in l:
            l = l.replace(part, "")
        return l
        
