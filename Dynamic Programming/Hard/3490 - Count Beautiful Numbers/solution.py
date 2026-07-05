class Solution(object):
    def maximumLength(self, nums):
        l = []
        for x in range(len(nums) ):
            l.append(str(nums[x]% 2))
        a = l.count("1")
        b = l.count("0")
        a = max(a, b)
        b=0
        for x in range(len(l)-1):
            if l[x]!=l[x+1]:
                b=b+1
        b=b+1
        return max(a, b)

        
