class Solution(object):
    def customSortString(self, order, s):
        a=""
        for x in order:
            if x in s:
                a=a+(x*s.count(x))
                s=s.replace(x,"")
        a=a+s
        return a

        
