class Solution(object):
    def detectCapitalUse(self, word):
        c=0
        l=["Q","W","E","R","T","Y","U","I","O","P","L","K","J","H","G","F","D","S","A","Z","X"
           ,"C","V","B","N","M"]

        g=["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","s","a","z","x"
           ,"c","v","b","n","m"]
        
        
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0] in l:
            for x in range(1,len(word)):
                if word[x] in l:
                    c=c+1
            if c>0:
                return False
            else:
                return True
        else:
            return False
                
        
