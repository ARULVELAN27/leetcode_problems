class Solution(object):
    def countPrefixSuffixPairs(self, w):
        a=0
        for x in range(0,len(w)-1):
            for y in range(x+1,len(w)):
                if x!=y and (w[y].startswith(w[x]) and w[y].endswith(w[x]) ):
                    a=a+1
        return a

        
