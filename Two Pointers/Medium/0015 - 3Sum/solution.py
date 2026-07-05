class Solution(object):
    def threeSum(self, nums):
        l1=[]
        nums.sort()
        for x in range(len(nums)):
            if x>0 and nums[x]==nums[x-1]:
                continue
            l=x+1
            r=len(nums)-1
            while l<r:
                if nums[x]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[x]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    l1.append([nums[x],nums[l],nums[r]])
                    le=nums[l]
                    while l<r and le==nums[l]:
                        l+=1
                    re=nums[r]
                    while l<r and re==nums[r]:
                        r-=1
        return l1
        
