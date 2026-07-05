class Solution(object):
    def myPow(self, x, n):
        c=str(n)
        if -100.0 < x and x < 100.0:
            if (-pow(2,31)) <= n and n <= (pow(2,31)-1):
                y=pow(x,n)
                if (-pow(10,4)) <= y <= pow(10,4):
                    return y
                else:
                    return 0
            else:
                return 0
        else:
            return 0
                    
                


        
       
       
