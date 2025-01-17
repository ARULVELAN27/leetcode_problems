class Solution(object):
    def countCharacters(self, words, chars):
        l=[]
        a=""
        k=""
        h=0
        for x in words:
            for y in x:
                if y not in chars or x.count(y)>chars.count(y):
                    a=""
                    break
                else:
                    a=a+y
            if a!=k:
                l.append(a)
            a=""
        for y in l:
            h=h+len(y)
        return h
    
            

        
