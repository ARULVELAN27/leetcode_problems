class Solution(object):
    def isCircularSentence(self, a):
        a = a.split(" ")
        a.append(a[0])
        for x in range(0,len(a)-1):
            if a[x][len(a[x])-1]!=a[x+1][0]:
                return False
        return True
        
