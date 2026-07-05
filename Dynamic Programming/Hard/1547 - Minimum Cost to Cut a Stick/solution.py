class Solution(object):
    def destCity(self, paths):
        a1=[]
        a2=[]
        for x in paths:
            a1.append(x[0])
            a2.append(x[1])
        for x in a2:
            if x not in a1:
                return x
        
        
