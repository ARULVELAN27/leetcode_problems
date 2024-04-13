class Solution(object):
    def frequencySort(self, nums):
        nums.sort(reverse=True)
        l=[]
        a=max(nums)
        for x in nums:
            if nums.count(x)<a:
                a=nums.count(x)
        while(len(nums)!=len(l)):
            for y in nums:
                if nums.count(y)==a:
                    l.append(y)
            a=a+1
        return l
         
        
