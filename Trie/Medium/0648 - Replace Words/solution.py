class Solution(object):
    def replaceWords(self, d, s):
        a=s.split()
        for x in d:
            for y in range(len(a)):
                if a[y].startswith(x)==True:
                    a[y]=x
        return " ".join(a)
        
        
