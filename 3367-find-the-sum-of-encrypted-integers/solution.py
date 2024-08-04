class Solution(object):
    def sumOfEncryptedInt(self, nums):
        out=0
        for x in nums:
            n=str(x)
            out+= int(max(n)*len(n))
        return out
            

        
