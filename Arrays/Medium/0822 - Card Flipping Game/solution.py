class Solution(object):
    def uniqueMorseRepresentations(self, words):
        a1=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l=[]
        a=""
        for x in words:
            for y in x:
                a = a + a1[ord(y) - 97 ]
            l.append(a)
            a=""
        return len(list(set(l)))
        


        
