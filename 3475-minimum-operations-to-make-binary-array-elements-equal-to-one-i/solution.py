class Solution(object):
    def minOperations(self, a):
        b=0
        for x in range(len(a)-2):
            if a[x]==0:
                b=b+1
                a[x:x+3]=list(map(lambda x: 0 if x == 1 else 1, a[x:x+3]))
        if len(set(a))==1 and a[0]==1:
            return b
        return -1 
            

        
