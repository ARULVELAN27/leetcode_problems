class Solution(object):
    def findDelayedArrivalTime(self, a, d):
        if a+d>23:
            return a+d-24
        return a+d
        
