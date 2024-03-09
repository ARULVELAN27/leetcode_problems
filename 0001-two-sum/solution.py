class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                a=nums[x]
                b=nums[y]
                c=a+b
                if c==target:
                    l.append(x)
                    l.append(y)
        return l
        
