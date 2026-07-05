class Solution(object):
    def largestAltitude(self, gain):
        c=[0]
        a=0
        for x in gain:
            a=a+x
            c.append(a)
        k=max(c)
        return k
        
