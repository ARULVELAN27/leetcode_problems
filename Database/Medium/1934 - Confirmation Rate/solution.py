class Solution(object):
    def evaluate(self, s, k):
        d={}
        l=0
        q=s[:]
        r=0
        b=""
        for x in k:
            d[x[0]]=x[1]
        for x in range(len(s)):
            if s[x]=="(":
                l=x
            elif s[x]==")":
                r=x
                if  s[l+1:r]  in d:
                    q = q.replace(s[l:r+1] , d[s[l+1:r]])
                else:
               
                    q=q.replace(s[l:r+1],"?")

        return q
            

            
