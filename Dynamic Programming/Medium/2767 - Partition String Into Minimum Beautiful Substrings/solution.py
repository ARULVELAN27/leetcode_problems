class Solution(object):
    def maximizeSum(self, nums, k):
        a=0
        b=max(nums)
        for x in range(1,k+1):
            a=a+max(nums)
            nums.remove(max(nums))
            nums.append(b+x)
        return a

        
        
