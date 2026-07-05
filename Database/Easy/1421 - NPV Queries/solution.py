class Solution(object):
    def findNumbers(self, nums):
        a=0
        for x in nums:
            if len(str(x))%2==0:
                a=a+1
        return a 
