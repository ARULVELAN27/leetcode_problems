class Solution(object):
    def numberOfSpecialChars(self, word):
        t=word
        a=0
        for x in word:
            if x.lower() in t and x.upper() in t:
                a+=1
                t=t.replace(x.lower(),"")
                t=t.replace(x.upper(),"")
        return a

            
