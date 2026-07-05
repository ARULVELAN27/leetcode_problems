class Solution(object):
    def divisorSubstrings(self, num, k):
        a=str(num)
        count=0
        b=""
        for x in a:
            b = b + x
            if len(b) > k:
                b = b[1:]
            if len(b) ==k and int(b)!=0 and num % int(b) == 0:
                count += 1
        return count
        
