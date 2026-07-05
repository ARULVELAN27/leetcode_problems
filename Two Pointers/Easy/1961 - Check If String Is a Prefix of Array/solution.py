class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        c=0
        p=0
        for x in costs:
            c=c+x
            p=p+1
            if c>coins:
                c=c-x
                p=p-1
        return p
        
