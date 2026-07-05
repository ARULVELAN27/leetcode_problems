class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        l=[]
        q=[]
        w=max(arr)
        if len(arr)==2:
            l.append(arr)
            return l
        for x in range(0,len(arr)-1):
            if arr[x+1]-arr[x]<w:
                w=arr[x+1]-arr[x]
        for x in range(0,len(arr)-1):
            if arr[x+1]-arr[x] == w:
                l.append(arr[x])
                l.append(arr[x+1])
                q.append(l)
                l=[]
        return q
        
