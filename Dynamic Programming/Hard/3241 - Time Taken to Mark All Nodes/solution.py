class Solution(object):
    def divideArray(self, nums, k):
        l=[]
        nums.sort()
        for x in range(0,len(nums),3):
            e=nums[x:x+3]
            if max(e)-min(e)>k:
                l=[]
                return l
            else:
                l.append(e)
        return l
