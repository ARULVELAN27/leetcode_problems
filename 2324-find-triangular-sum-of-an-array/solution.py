class Solution(object):
    def triangularSum(self, nums):
        nums2=[]
        while len(nums)>1:
            for x in range(0,len(nums)-1):
                a=nums[x]+nums[x+1]
                if a>10:
                    a=a%10
                    nums2.append(a)
                else:
                    nums2.append(a)
                a=0
            nums=[]
            for y in nums2:
                nums.append(y)
            nums2=[]
        return nums[0]%10
