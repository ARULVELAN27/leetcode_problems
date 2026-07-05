class Solution(object):
    def vowelStrings(self, words, left, right):
        vo=["a","e","i","o","u"]
        a=0
        for x in range(left,right+1):
            if words[x][0] in vo and (words[x][len(words[x])-1] in vo):
                a=a+1
        return a
            

        
