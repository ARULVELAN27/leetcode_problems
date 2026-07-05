class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        l=sentence.split()
        a=0
        for x in range(0,len(l)):
            if l[x].startswith(searchWord):
                a=x+1
                break
        if a==0:
            return -1
        return a
        
