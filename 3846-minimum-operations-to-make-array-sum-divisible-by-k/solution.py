class Solution(object):
    def minOperations(self, nums, k):
        a=sum(nums)
        b=0
        while a%k!=0:
            a=a-1
            b+=1
        return b
        
