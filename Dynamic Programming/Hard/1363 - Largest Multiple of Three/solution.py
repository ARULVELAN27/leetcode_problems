class Solution(object):
    def greatestLetter(self, s):
        t=s
        a=""
        for x in s:
            if x.lower() in t and x.upper() in t:
                a=a+x.upper()
        if len(a)==0:
            return a
        p=list(a)
        p.sort(reverse=True)
        return p[0]
        

        
