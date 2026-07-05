class Solution(object):
    def mostWordsFound(self, sentences):
        c=0
        l=[]
        for x in sentences:
            for y in x:
                if y==" ":
                    c=c+1
            s=c+1
            l.append(s)
            c=0
            
        g=max(l)
        return g       
