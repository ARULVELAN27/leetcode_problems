class Solution(object):
    def numberOfPairs(self, nums):
        even=0
        odd=0
        l=[]
        a=list(set(nums))
        for x in a:
            if nums.count(x)%2==0:
                even+=nums.count(x)/2
            else:
                even+=((nums.count(x)-1)/2)
                odd=odd+1
        l.append(even)
        l.append(odd)
        return l
