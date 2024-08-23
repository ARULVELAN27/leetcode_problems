class Solution(object):
    def sortSentence(self, s):
        a=s.split()
        l=[]
        for y in range(0,len(a)):
            for x in range(0, len(a) - 1):
                q = a[x]
                w = a[x + 1]
                if int(q[len(q) - 1]) > int(w[len(w) - 1]):
                    e = a[x]
                    a[x] = a[x + 1]
                    a[x + 1] = e
        for z in a:
            l.append(z[:len(z)-1])
        q=" ".join(l)
        return q

            
            
        
            
        
