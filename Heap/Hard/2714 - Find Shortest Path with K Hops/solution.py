class Solution(object):
    def leftRightDifference(self, nums):
        l=[]
        for x in range(0,len(nums)):
            les=0
            ris=0
            for y in range(0,x):
                les=les+nums[y]
            for z in range(x+1,len(nums)):
                ris=ris+nums[z]
            l.append(abs(les - ris))
        return l
