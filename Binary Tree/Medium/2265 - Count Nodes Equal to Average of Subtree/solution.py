class Solution(object):
    def pivotArray(self, nums, pivot):
        l=[]
        e=[]
        for x in nums:
            if x <pivot:
                l.append(x)
            elif x>pivot:
                e.append(x)
            else:
                e.insert(0,pivot)
        
        return l+e
