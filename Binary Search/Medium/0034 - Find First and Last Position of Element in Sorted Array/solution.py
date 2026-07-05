class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        a=[-1,-1]
        c=[]
        if len(nums)==0:
            return a
        for x in range(0,len(nums)):
            if target in nums:
                if nums[x] == target:
                    l.append(x)
            else:
                return a
        if len(l)==1:
            l.append(l[0])
        if len(l)>2:
            c.append(min(l))
            c.append(max(l))
            return c
        return l
            

        
