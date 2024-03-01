class Solution(object):
    def thirdMax(self, nums):
        l=[]
        if len(nums)<3:
            nums.sort()
            z=len(nums)-1
            return nums[z]
        else:
            for x in nums:
                if x  not in l:
                    l.append(x)

            if len(l)<3:
                nums.sort()
                z=len(nums)-1
                return nums[z]
            else:
                l.sort()
                z = len(l) - 3
                return l[z]
            
            
