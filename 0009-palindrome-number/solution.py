class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        l = []
        e = len(a)
        i=0
        j=len(a)-1
        for  q in a:
           l.append(q)
        for s in range(e):
            if l[i] == l[j]:
                i = i + 1
                j = j - 1
                r = True
            else:
                r = False
        print(r)
        return(r)



    

        
        
