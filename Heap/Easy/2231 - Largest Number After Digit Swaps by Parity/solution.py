class Solution(object):
    def firstPalindrome(self, words):
        for x in range(0,len(words)):
            a=words[x]
            if a==a[::-1]:
                return words[x]
        return ""

        
