class Solution(object):
    def majorityElement(self, v):
            a = {}
            g=[]
            for x in range(0, len(v)):
                c=v[x]
                if a.get(c):
                    h=a.get(c)
                    f=h+1
                    a.update({c: f})
                else:
                    a[c] = 1
            for y in a.values():
                g.append(y)
            i=max(g)
            key = list(filter(lambda x: a[x] == i, a))[0]
            return key
        
        
        
