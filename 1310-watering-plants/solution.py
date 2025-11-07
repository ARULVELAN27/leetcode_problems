class Solution(object):
    def wateringPlants(self, a, c):
        index=0
        q=0
        p=c
        while(a[-1]!=0):
            if a[index]<=c:
                c=c-a[index]
                a[index]=0
                index=index+1
                q=q+1
            else:
                c=p
                q=q+(index*2)+1
                c=c-a[index]
                a[index]=0
                index =index+1
        return q

        
