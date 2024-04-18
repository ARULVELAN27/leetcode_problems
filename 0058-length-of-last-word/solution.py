class Solution(object):
    def lengthOfLastWord(self, s):
        a=0
        b=0
        for x in range(len(s)-1,-1,-1):
            if s[x]==" ":
                a=a+1
            else:
                for z in range(len(s)-1-a,-1,-1):
                    if s[z]==" ":
                        return b
                    else:
                        b=b+1 
                return b         
