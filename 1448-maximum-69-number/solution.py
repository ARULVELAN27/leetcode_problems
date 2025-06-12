class Solution(object):
    def maximum69Number (self, nums):
        a=0
        b=""
        nums=str(nums)
        for x in range(len(nums)):
            if nums[x]=="6":
                b=b+("9")
                b=b+nums[x+1:len(nums)]
                break
            else:
                b=b+(nums[x])
        return int(b)

        
