class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        a=0
        
        
        for x in range(0,len(cost),3):
            if len(cost)<3:
                for x in range(0,len(cost)):
                    a=a+cost[0]
                    cost.pop(0)
            else:
                a=a+cost[0]+cost[1]
                for z in range(0,3):
                    cost.pop(0)
                
        return a

        
