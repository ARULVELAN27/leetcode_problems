class Solution(object):
    def findRestaurant(self, l, l1):
        
        g=[]
        p=[]
        h=[]
        u=0
        for x in range(0,len(l)):
            for y in range(0,len(l1)):
                if l[x]==l1[y]:
                    a=l[x]
                    c=x+y
                    g.append(a)
                    p.append(c)
        r=min(p)
        for x in range(0,len(p)):
            j=p[x]
            if j==r:
                h.append(g[x])
        return h
        

                    
        

        


        
