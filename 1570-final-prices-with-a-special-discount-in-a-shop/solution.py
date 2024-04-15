class Solution(object):
    def finalPrices(self, prices):
        l=[]
        for x in range(0,len(prices)):
            for y in range(x+1,len(prices)):
                if prices[x]>=prices[y]:
                    l.append(prices[x]-prices[y])
                    break
            else:
                l.append(prices[x])
        return l
