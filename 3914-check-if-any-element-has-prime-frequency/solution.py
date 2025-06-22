class Solution(object):
    def checkPrimeFrequency(self, nums):
        a=0
        for x in nums:
            if nums.count(x)>1:
                for y in range(1,nums.count(x)):
                    if (nums.count(x))%y==0:
                        a=a+1
                if a==1:
                    return True
                else:
                    a=0
        return False
                
        
