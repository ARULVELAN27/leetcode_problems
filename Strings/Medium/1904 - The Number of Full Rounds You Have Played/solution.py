class Solution(object):
    def secondHighest(self, s):
        l = []
        for x in s[::-1]:
            if x.isnumeric() == True and x not in l:
                l.append(x)
        l.sort(reverse=True)
        if len(l)==1 or len(l)==0:
            return -1
        return int(l[1])
        
