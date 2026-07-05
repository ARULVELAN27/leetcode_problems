class Solution(object):
    def generateTag(self, c):
        c= c.strip()
        a=c.split(" ")
        g="".join([x.capitalize() for  x in a[1:len(a)]])
        y="#"+a[0].lower()+g
        if len(y)>100:
            return y[0:100]
        return y
        
