class Solution(object):
    def rearrangeArray(self, nums):
        g=[]
        l=[]
        rank=[]
        for x in nums:
            if x>0:
                g.append(x)
            else:
                l.append(x)
        for y in range(0,int(len(nums))/2):
            rank.append(g[y])
            rank.append(l[y])
        return rank
        
