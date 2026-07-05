class Solution(object):
    def reverseDegree(self, s):
        a=0
        for x in range(1,len(s)+1):
            a=a+(x*(ord(s[x-1])-71-(2*(ord(s[x-1])-97))))
        return a
