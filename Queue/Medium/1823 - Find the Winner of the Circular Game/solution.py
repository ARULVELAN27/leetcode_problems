class Solution(object):
    def halvesAreAlike(self, s):
        i=0
        g=0
        l=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a=s[:int((len(s)/2))]
        b=s[int((len(s)/2)):]
        for x in a :
            if x in l:
                i=i+1
        for x in b:
            if x in l:
                g=g+1
        if i==g:
            return True
        return False
