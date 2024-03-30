class Solution(object):
    def shuffle(self, nums, n):

        l=[]
        l1=[]
        l2=[]
        r=1
        for x in range(0,int(len(nums)/2)):
            l.append(nums[x])
            l1.append(nums[x+int(len(nums)/2)])
        for y in range(0,int(len(nums)/2)):
            l.insert(y+r,l1[y])
            r=r+1
        return l


