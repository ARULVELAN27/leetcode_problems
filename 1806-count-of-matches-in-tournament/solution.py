class Solution(object):
    def numberOfMatches(self, n):
        a=0
        l=[]
        while(n!=1):
            if n%2==0:
                l.append(n/2)
                n=n/2
            else:
                l.append((n - 1) / 2)
                n=((n-1)/2)+1
        return sum(l)
        
