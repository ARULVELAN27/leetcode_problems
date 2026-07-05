class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        a=[]
        b=[]
        w=0
        for x in range(0,len(jewels)):
            a.append(jewels[x])
        for x in range(0,len(stones)):
            b.append(stones[x])
        for y in a:
            w=w+b.count(y)
        return w
