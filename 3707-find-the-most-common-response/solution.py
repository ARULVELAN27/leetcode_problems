class Solution(object):
    def findCommonResponse(self, r):
        l=[]
        for x in r:
            l.extend(list(set(x)))
        d={}
        best=None
        bcnt=0
        for x in l:
            cnt=d.get(x,0)+1
            d[x]=cnt
            if cnt>bcnt or (cnt==bcnt and (best is None or x<best)):
                bcnt=cnt
                best=x
        return best
        
