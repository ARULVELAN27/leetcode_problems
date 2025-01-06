import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        a = re.sub(r'[^a-zA-Z0-9]', ' ', paragraph)
        b=a.lower()
        s=b.split(" ")
        for x in range(s.count("")):
            s.remove("")
        c=0
        p=""
        for x in s:
            if x not in banned and s.count(x)>c:
                c=s.count(x)
                p=x
        return p
        
