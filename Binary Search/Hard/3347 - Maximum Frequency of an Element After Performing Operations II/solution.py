class Solution(object):
    def resultArray(self, nums):
        a=[nums[0]]
        b=[nums[1]]
        for x in nums[2:len(nums)]:
            if a[len(a)-1]>b[len(b)-1]:
                a.append(x)
            else:
                b.append(x)
        return a+b
        
