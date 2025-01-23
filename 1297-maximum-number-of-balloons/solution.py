class Solution(object):
    def maxNumberOfBalloons(self, text):
        a="balloon"
        l=[]
        for x in a:
            if x=="l" or x=="o":
                l.append(int(text.count(x)/2))
            else:
                l.append(text.count(x))
            
        return min(l)
        
