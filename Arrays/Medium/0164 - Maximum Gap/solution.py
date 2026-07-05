class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        k=[]
        if len(nums)>1:
            for x in range(0,len(nums)-1):
                y=x+1
                d=nums[y]-nums[x]
                k.append(d)
            s=max(k)
            return s
        else:
            return 0

        
