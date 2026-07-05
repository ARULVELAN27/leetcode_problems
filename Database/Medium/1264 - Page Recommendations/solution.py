class Solution(object):
    def canBeTypedWords(self, text, q):
        l=[]
        r=""
        a=text.split()
        if len(q)==0:
            return len(a)
        for x in a:
            for y  in q:
                if y not in x:
                    r=x
                else:
                    r=""
                    break
            l.append(r)
        return len(l)-l.count("")

        
