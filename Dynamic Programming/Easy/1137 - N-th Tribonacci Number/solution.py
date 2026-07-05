class Solution(object):
    def heightChecker(self, heights):
        l=[]
        t=0
        for x in heights:
            l.append(x)
        l.sort()
        for r in range(0,len(heights)):
            if heights[r]!=l[r]:
                t=t+1
        return t
        
