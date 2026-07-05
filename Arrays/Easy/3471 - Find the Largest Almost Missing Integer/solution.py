class Solution(object):
    def minimumAverage(self, nums):
        a=[]
        for x in range(0,int(len(nums)/2)):
            s=float(max(nums)+min(nums))/2
            a.append(s)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(a)
