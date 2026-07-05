class Solution(object):
    def countTestedDevices(self, a):
        b=0
        for x in range(0,len(a)):
            if a[x]!=0:
                b=b+1
                for u in range(x,len(a)):
                    if a[u]>0 :
                        a[u]=a[u]-1
        return b

        
