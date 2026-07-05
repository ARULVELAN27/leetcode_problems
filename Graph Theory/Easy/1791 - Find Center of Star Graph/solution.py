class Solution(object):
    def maximumWealth(self, accounts):
        a=0
        b=0
        l=[]
        for x in accounts:
            for y in x:
                b=b+y
            l.append(b)
            b=0
        return max(l)

        
