class Solution(object):
    def threeSumClosest(self, nums, target):
        best=float('inf')
        nums.sort()
        for x in range(len(nums)-2):
            if x>0 and nums[x]==nums[x-1]:
                continue
            l=x+1
            r=len(nums)-1
            while l<r:
                a=nums[x]+nums[l]+nums[r]
                d=a-target
                if abs(d)<best:
                    best=abs(d)
                    ret=a
                if d<0:
                    l+=1
                elif d>0:
                    r-=1
                else:
                    return a
        return ret
