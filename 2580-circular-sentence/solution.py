class Solution(object):
    def isCircularSentence(self, s):
        a=s.split(" ")
        for x in range(len(a)):
            if a[x][len(a[x])-1]!=a[(x+1)%len(a)][0]:
                return False
        return True
        
