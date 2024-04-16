class Solution(object):
    def findWordsContaining(self, words, x):
        l=[]
        for r in range(0,len(words)):
            for y in words[r]:
                if y==x:
                    l.append(r)
                    break
        return l
        
