class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=max(candies)
        l=[]
        for x in candies:
            if x+extraCandies>=a:
                l.append(True)
            else:
                l.append(False)
        return l
        
