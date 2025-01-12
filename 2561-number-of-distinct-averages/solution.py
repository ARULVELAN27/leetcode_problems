class Solution(object):
    def distinctAverages(self, nums):
        l=[]
        while len(nums)>0:
            a=max(nums)
            b=min(nums)
            l.append((float(a+b))/2)
            nums.remove(a)
            nums.remove(b)
        return len(set(l))
