class Solution(object):
    def possibleStringCount(self, word):
        a=1
        for x in range(1,len(word)):
            if word[x]==word[x-1]:
                a+=1
        return a
        
        
