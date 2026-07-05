class Solution(object):
    def isValid(self, word):
        p="aeiouAEIOU"
        v=False
        c=False
        for x in word:
            if x in p and x.isnumeric()==False:
                v=True
            elif x not in p and x.isnumeric()==False:
                c=True
        if v==True and c==True and word.isalnum()==True and len(word)>2:
            return True
        return False


        
