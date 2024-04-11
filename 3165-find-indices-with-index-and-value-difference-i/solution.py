class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        l=[]
        l1=[]
        for x in range(0,len(nums)):
            for y in range(0,len(nums)):
                if (abs(x-y)>=indexDifference) and (abs(nums[x]-nums[y])>=valueDifference):
                    l.append(x)
                    l.append(y)
                    l1.append(l)
                    l=[]
        if len(l1)>0:
            return l1[0]
        else:
            return [-1,-1]

        
