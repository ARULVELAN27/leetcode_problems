class Solution(object):
    def firstUniqChar(self, s):
        l=[]
        l1=[]
        l2=[]
        for x in s:
            l.append(x)
        for y in l:
            if y not in l1:
                l1.append(y)
        for z in l1:
            r=l.count(z)
            l2.append(r)
        for g in range(0,len(l2)):
            if l2[g]==1:
                s=l1[g]
                for x in range(0,len(l)):
                    if l[x]==s:
                        return x
        return -1

    
        
