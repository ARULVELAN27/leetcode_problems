class Solution(object):
    def stringMatching(self, words):
        a=[]
        for x in words:
            for y in words:
                if x!=y and x in y:
                    a.append(x)
        return list(set(a))        
