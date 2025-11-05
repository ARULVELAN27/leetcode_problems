class Solution(object):
    def findLonely(self, nums):

        a={}
        for n in nums:
            a[n]=a.get(n,0)+1
        l=[]
        for n in nums:
            if a[n]==1 and (n-1) not in a and (n+1) not in a:
                l.append(n)
        return l

        

