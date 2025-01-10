class Solution(object):
    def kLengthApart(self, nums, k):
        l=[]
        for x in range(len(nums)):
            if nums[x]==1:
                l.append(x)

        for y in range(len(l)-1):
            if abs(l[y]-l[y+1])<=k:
                return False
        return True


        
