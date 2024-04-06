class Solution(object):
    def removeDuplicates(self, nums):
        a=[]
        for x in nums:
            if nums.count(x)>1:
                for z in range(0,nums.count(x)-1):
                    nums.remove(x) 
        return len(nums)
        
