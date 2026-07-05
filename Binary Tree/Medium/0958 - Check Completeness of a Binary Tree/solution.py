class Solution(object):
    def sortArrayByParityII(self, nums):
        odd=[]
        even=[]
        rank=[]
        for x in nums:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        for y in range(0,int(len(nums))/2):
            rank.append(even[y])
            rank.append(odd[y])
        return rank

        
