class Solution(object):
    def countPairs(self, nums, target):
        b=len(nums)
        p=b-1
        j=0
        for x in range(0,b):
            if x!=p:
                c=x+1
                for y in range(c,b):
                    s=nums[x]+nums[y]
                    if s<target:
                        j=j+1
            else:
                return j

