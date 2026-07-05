class Solution(object):
    def findDifferentBinaryString(self, nums):
        nums.sort()
        for x in range(0,int(len(nums)*"1",2)+1):
            a=((len(nums[0])-len(bin(x)[2:]))*"0")+bin(x)[2:]
            if a not in nums:
                return a
    



        
        
