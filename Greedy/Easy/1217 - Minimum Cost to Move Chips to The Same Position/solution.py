class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        l=[]
        l1=[]
        for x in range(0,len(arr2)):
            for y in range(0,len(arr1)):
                if arr2[x]==arr1[y]:
                    l.append(arr1[y])
        arr1.sort()          
        for d in arr1:
            if d not in arr2:
                l.append(d)
        return l

               
        
        
