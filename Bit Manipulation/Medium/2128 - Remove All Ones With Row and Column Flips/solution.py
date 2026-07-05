class Solution(object):
    def reversePrefix(self, a, ch):
        for x in range(0,len(a)) :
            if ch not in a:
                return a
            elif a[x]==ch:
                return a[:x+1][::-1] + a[x+1:]
 
