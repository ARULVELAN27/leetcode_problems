class Solution(object):
    def createTargetArray(self, nums, index):
        l=[]
        for x in range(0,len(index)):
            l.insert(index[x],nums[x])
        return l
        
