class Solution(object):
    def merge(self, nums):
        nums.sort()
        l=[]
        while(len(nums)>1):
            if ((nums[0][0]==nums[1][0]) and (nums[0][1]==nums[1][1])):
                nums.pop(0)
            elif (nums[0][1]>=nums[1][0] and (nums[0][1]<nums[1][1])):
                p=[nums[0][0],nums[1][1]]
                nums.pop(0)
                nums.pop(0)
                if len(nums)==0:
                    l.append(p)
                else:
                    nums.insert(0,p)
            elif ((nums[0][1]>=nums[1][0]) and (nums[0][1]>=nums[1][1]) ):
                p=nums[0]
                nums.pop(0)
                nums.pop(0)
                if len(nums)==0:
                    l.append(p)
                else:
                    nums.insert(0,p)
            else:
                l.append(nums[0])
                nums.pop(0)
        if len(nums)==1:
            l.append(nums[0])
        return l     
        
