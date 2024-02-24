class Solution(object):
    def singleNumber(self, nums):
        l=[]
        c=0
        for i in range(len(nums)):
            if(nums.count(nums[i])==1):
                l.append(nums[i])
            else:
                c=c+1
        return l

        
