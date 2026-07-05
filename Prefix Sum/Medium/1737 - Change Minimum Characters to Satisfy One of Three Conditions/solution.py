class Solution(object):
    def maxDepth(self, s):
        a=0
        b=0
        l=[]
        for x in range(len(s)):
            if len(l)==0 or s[x]=="(" :
                l.append(s[x])
                a=l.count("(")
                if a>b:
                    b=a 
            elif s[x] ==")" and l[len(l)-1]=="(":
                l.pop()
        return b


        
