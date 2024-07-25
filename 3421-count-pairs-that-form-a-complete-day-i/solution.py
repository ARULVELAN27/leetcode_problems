class Solution(object):
    def countCompleteDayPairs(self, hours):
        a=0
        for x in range(0,len(hours)):
            for y in range(x+1,len(hours)):
                if (hours[x]+hours[y])%24==0:
                    a=a+1
        return a
        
