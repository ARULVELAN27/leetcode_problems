class Solution(object):
    def recoverOrder(self, order, friends):
        l=[]
        for x in order:
            if x in friends:
                l.append(x)
        return l
        
