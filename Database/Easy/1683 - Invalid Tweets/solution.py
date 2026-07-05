class Solution(object):
    def maxCoins(self, piles):
        c = len(piles) // 3   
        piles.sort(reverse=True)
        a = 0
        total = 0
        w = 0

        for x in piles:
            if a == 1:
                total += x
                a = 0
                w += 1
            else:
                a = 1
            if w == c:
                break

        return total

        
