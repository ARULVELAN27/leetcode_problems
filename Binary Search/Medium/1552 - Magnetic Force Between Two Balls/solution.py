class Solution(object):
    def buildArray(self, target, n):
        l=[]
        p=[]
        for x in range(1,n+1):
            if p==target:
                return l
            elif x not in target:
                l.append("Push")
                p.append(x)
                l.append("Pop")
                p.pop()
            else:
                l.append("Push")
                p.append(x)
        return l
            

        
