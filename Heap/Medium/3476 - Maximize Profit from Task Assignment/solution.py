class Solution(object):
    def minimumOperations(self, nums):
        a=0
        for x in nums:
            if x%3==0:
                a=a+0
            else:
                for y in range(1,4):
                    if (x+y)%3==0:
                        a=a+y
                        break
                    elif (x-y)%3==0:
                        a=a+y
                        break
        return a

        
