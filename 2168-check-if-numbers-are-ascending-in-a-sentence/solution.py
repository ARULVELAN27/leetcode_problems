import re
class Solution(object):
    def areNumbersAscending(self, s):
        l=[]
        a=re.split("[^0-9]*",s)
        for x in a :
            if x!='':
                l.append(int(x))
        for y in range(0,len(l)-1):
            if l[y]>=l[y+1]:
                return False
        return True
        
