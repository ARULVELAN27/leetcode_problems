class Solution(object):
    def lastStoneWeight(self, stones):
        for x in range(len(stones)):
            if len(stones)==0:
                return 0

            elif len(stones)==1:
                return stones[0]
            else:
                a=max(stones)
                stones.remove(a)
                b=max(stones)
                stones.remove(b)
                if a!=b:
                    stones.append(abs(a-b))
 

        
