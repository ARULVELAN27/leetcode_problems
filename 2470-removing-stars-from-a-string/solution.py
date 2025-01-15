class Solution(object):
    def removeStars(self, s):
        l=[]
        for x in s:
            if x=="*":
                l.pop()
            else:
                l+=[x]
        return "".join(l)
        
