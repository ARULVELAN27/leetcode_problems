class Solution(object):
    def beautifulArray(self, n):
        l=[1]
        odd=[]
        even=[]
        for x in range(2,n+1):
            for y in l:
                if ((2*y)-1)<=x:
                    odd.append((2*y)-1) 
                if 2*y<=x:
                    even.append(2*y)
            l=[]
            l=odd+even
            odd=[]
            even=[]
        return l
        return l
        
