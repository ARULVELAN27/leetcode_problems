class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        e=[]
        g=[]
        p=[]
        r=[]
        f="_"
        for x in range(len(code)):
            i=code[x]
            if all(x.isalnum() or x == '_' for x in i) and (len(i)>0  and (isActive[x]==True)):
                print(i)
                if businessLine[x]=="electronics":
                    e.append(code[x])
                elif businessLine[x]=="grocery":
                    g.append(code[x])
                elif businessLine[x]=="pharmacy":
                    p.append(code[x])
                elif businessLine[x]=="restaurant":
                    r.append(code[x])
        e.sort()
        g.sort()
        p.sort()
        r.sort()
        return e+g+p+r
        
