class Solution(object):
    def countSubarrays(self, nums, k):
        a=max(nums)
        n=len(nums)
        count=0
        ans=0
        start=0
        for x in range(n):
            if nums[x]==a:
                count=count+1
            while count>=k:
                ans=ans+(n-x)
                if nums[start]==a:
                    count-=1
                start+=1
        return ans


