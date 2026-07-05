class Solution(object):
    def reverseWords(self, s):
        a=s.split()
     
        w=" ".join(a[::-1])
        return w
        
