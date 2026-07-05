class Solution(object):
    def compressedString(self, word):
        comp=""
        count=0
        d=""
        for x in word:
            if count==9 or x!=d and d!="":
                comp=comp+str(count)+d
                count=1
            else:
                count=count+1
            d=x
        comp=comp+str(count)+d
        return comp

        
