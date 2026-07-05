class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        a=""
        b=""
        c=""
        for x in firstWord:
            a=a+str(ord(x)-97)
        for x in secondWord:
            b=b+str(ord(x)-97) 
        for x in targetWord:
            c=c+str(ord(x)-97) 
        b = str(int(a) + int(b))
        if int(b)== int(c):
            return True
        return False 

        
        
