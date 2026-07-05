class Solution(object):
    def removeOuterParentheses(self,t):
        a=0
        b=0
        l=[]
        s=""
        for x in t:
            if x=="(":
                a=a+1
                s=s+x
            elif x==")":
                b=b+1
                s=s+x
            if a==b:
                l.append(s[1:len(s)-1])
                s=""
        return "".join(l)
            

            


        
