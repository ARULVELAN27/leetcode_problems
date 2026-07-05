class Solution(object):
    def strStr(self, haystack, needle):
        a=-1
        if needle in haystack:
            a=haystack.index(needle)
        return a

        
