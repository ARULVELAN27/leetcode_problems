class Solution(object):
    def longestPalindrome(self, s):
        a=""
        for x in range(1,len(s)+1):
            for y in range(len(s)-x+1):
                r=s[y:y+x]
                f=r[::-1]
                if f==r and len(r)>len(a): 
                    a=r
        return a
        
