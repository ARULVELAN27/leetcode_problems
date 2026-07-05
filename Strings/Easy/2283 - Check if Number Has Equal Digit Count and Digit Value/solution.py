class Solution(object):
    def sortEvenOdd(self, nums):
        odd=[]
        even=[]
        for x in range(0,len(nums)):
            if x%2==0:
                even.append(nums[x])
            else:
                odd.append(nums[x])
            even.sort()
            odd.sort(reverse=True)
        a=1
        for x in odd:
            even.insert(a,x)
            a=a+2
        return even
