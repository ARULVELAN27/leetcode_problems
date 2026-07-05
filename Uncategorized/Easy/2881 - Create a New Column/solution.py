class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        l=[]
        for x in words:
            s=x.split(separator)
            for t in s:
                l.append(t)
        for x in range(0,l.count("")):
            l.remove("")
        return l
        
        
