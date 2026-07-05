class Solution(object):
    def findMaxAverage(self, nums, k):
        sum1=0
        count=0
        c=0
        a=0
        max1=min(nums)
        for x in nums:
            sum1=sum1+x
            c=c+1
            if c==k:
                a=sum1/float(k)
                if a>max1:
                    max1=a
            
            if c>=k:
                sum1-=nums[count]
                count+=1
                c-=1
        return max1

