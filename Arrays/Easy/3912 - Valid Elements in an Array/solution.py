class Solution(object):
    def concatHex36(self, n):
        a = n * n
        k = ""
        p = ""
        q = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        while a >= 1:
            k = q[int(a % 16)] + k
            a = a / 16


        a = n * n * n
        while a >= 1:
            p = q[int(a % 36)] + p
            a = a / 36

        return k+p

            



        
