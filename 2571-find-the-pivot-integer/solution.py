class Solution(object):
    def pivotInteger(self, n):
        pivot=1
        left=0
        right=0
        while(pivot<=n):
            left=(pivot*(pivot+1))//2
            right=((abs(pivot-n)+1)*(pivot+n))//2
            print(left,right)
            if left==right:
                return pivot
            else:
                pivot=pivot+1
        return -1

        
