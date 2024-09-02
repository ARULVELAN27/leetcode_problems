class Solution(object):
    def countKeyChanges(self, s):
        a=0
    
        b=s.lower()
        for x in range(0,len(b)-1):
            if b[x]!=b[x+1]:
                a=a+1
        return a
        
