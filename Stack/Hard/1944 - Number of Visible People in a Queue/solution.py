class Solution(object):
    def truncateSentence(self, s, k):
        a=s.split()
        w=""
        for x in range(0,k):
            w=w+a[x]
            if x==k-1:
                break
            else:
                w=w+" "
        return w

        
