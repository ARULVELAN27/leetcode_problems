class Solution(object):
    def decompressRLElist(self, nums):
        e=[]
        for x in range(0,len(nums),2):
            e=e+([nums[x+1]]*nums[x])
        return e
        
