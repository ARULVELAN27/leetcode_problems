class Solution(object):
    def nextGreatestLetter(self, letters, target):
        a=ord(target)
        p=letters[0]
        l=[]
        for x in letters:
            b=ord(x)
            if b>a:
                l.append(x)
        
        l.sort()
        if len(l)>0:
            h=l[0]
            return h
        else:
            return p
        
        
