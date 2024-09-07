class Solution(object):
    def isPalindrome(self, s):
        w=s.lower()
        a=['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','M','N','B','V','C','X','Z','1','2','3','4','5','6','7','8','9','0']
        for x in s:
            if x not in a :
                w=w.replace(x,"")
        q=w.split()
        o="".join(q)
        if o==o[::-1]:
            return True
        
        
