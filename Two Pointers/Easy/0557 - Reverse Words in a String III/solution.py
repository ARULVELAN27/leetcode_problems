class Solution(object):
    def reverseWords(self, s):
        a=""
        b=s.split()
        for x in range(0,len(b)):
            a=a+b[x][::-1]
            if x!=len(b)-1:
                a=a+" "
        return a
        
