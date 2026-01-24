class Solution(object):
    
    def solu(self,nums,k):
        l=0
        odd_count=0
        count1=0
        for x in range(len(nums)):
            if nums[x]%2!=0:
                odd_count+=1
            while odd_count>k:
                if nums[l]%2!=0:
                    odd_count-=1
                l+=1
            count1+=x-l+1

        return count1
    def numberOfSubarrays(self, nums, k):
        return self.solu(nums,k)-self.solu(nums,k-1)
            
