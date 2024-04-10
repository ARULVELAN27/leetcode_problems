class Solution(object):
    def moveZeroes(self, nums):
        a=0
        for t in range(0,nums.count(0)):
            for x in nums:
                if x==0:
                    nums.remove(0)
                    a=a+1
        for y in range(0,a):
            nums.append(0)
        return nums
        
