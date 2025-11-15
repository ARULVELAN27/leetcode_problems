class Solution(object):
    def containsDuplicate(self, nums):
        a={}
        for x in nums:
            if x in a:
                return True
            else:
                a[x]=0
        return False
        
