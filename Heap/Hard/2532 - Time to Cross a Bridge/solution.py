class Solution(object):
    def equalFrequency(self, word):
        l=[]
        for x in range(len(word)):
            a=word[0:x]+word[x+1:len(word)]
            a=list(a)
            for x in a:
                l.append(a.count(x))
            if len(set(l))==1:
                return True
            l=[]
        return False

        
