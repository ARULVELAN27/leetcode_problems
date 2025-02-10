class Solution(object):
    def maximumOddBinaryNumber(self, s):
        a = s.count("1")
        s=s.replace("1", "0")
        s = s[0:len(s) - 1] + "1"
        a = a - 1
        s = "1" * a + s[a:len(s)]
        return s


        
