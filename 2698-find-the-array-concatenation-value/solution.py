class Solution(object):
    def findTheArrayConcVal(self, nums):
        c=0
        for x in range(0,int(len(nums)/2)+1):
            if len(nums)>1:
                a=str(nums[0])+str(nums[len(nums)-1])
                nums.pop(0)
                nums.pop(len(nums)-1)
                c=c+int(a)
            elif len(nums)==1:
                c=c+nums[0]
        return c


        
