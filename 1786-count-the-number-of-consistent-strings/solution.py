class Solution(object):
    def countConsistentStrings(self, allowed, words):
        a=0
        for x in words:
            for y in x:
                if y  not in allowed:
                    break
            else:
                a=a+1
        return a 

        
