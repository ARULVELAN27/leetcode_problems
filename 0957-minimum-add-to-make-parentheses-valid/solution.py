class Solution(object):
    def minAddToMakeValid(self, s):
        l=[]
        for x in s:
            if len(l)>0 and x==")" and l[len(l)-1]=="("  :
                l.pop()
            else:
                l.append(x)
        return len(l)
        
