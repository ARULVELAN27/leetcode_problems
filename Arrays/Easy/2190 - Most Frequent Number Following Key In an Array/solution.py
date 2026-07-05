class Solution(object):
    def countWords(self, words1, words2):
        a=0
        for x in words1:
            if x in words2 and words1.count(x)==1 and words2.count(x)==1:
                a=a+1
        return a
        
