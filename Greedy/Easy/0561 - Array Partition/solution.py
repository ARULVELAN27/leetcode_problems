class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort(reverse=True)
        e=0
        for x in range(0,len(nums),2):
            e=e+min(nums[x],nums[x+1])
        return e
                                                  
            



        
