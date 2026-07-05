class Solution(object):
    def largestOddNumber(self, num):
        a=int(num)
        for x in range(0,len(num)):
            if a%2==0:
                a=int(a/10)
            else:
                return str(a)
        return ""
        
