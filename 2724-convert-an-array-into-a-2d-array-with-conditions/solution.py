class Solution(object):
    def findMatrix(self, nums):
        l=[]
        l1=[]
        while(len(nums)>0):
            for x in nums:
                if x not in l:
                    l.append(x)
            l1.append(l)
            for x in l:
                nums.remove(x)
            l=[]
        return l1
        
