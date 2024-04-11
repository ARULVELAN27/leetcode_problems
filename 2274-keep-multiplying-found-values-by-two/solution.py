class Solution(object):
    def findFinalValue(self, nums, original):
        i=1
        while(i==1):
            if original in nums:
                original=original*2
            else:
                return original

        
