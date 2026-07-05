class Solution(object):
    def distributeCandies(self, candyType):
        a=list(set(candyType))
        if len(a)>(len(candyType)/2):
            return len(candyType)/2
        else:
            return len(a)
        
