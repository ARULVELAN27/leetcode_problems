class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        a=0
        for x in range(0,len(words)-1):
            for y in range(x+1,len(words)):
                if words[x]==words[y][::-1]:
                    a=a+1
        return a

        
