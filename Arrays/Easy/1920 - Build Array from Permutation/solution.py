class Solution(object):
    def squareIsWhite(self, coordinates):
        p=coordinates[0]
        q=int(coordinates[1])
        if p=="a" or p=="c" or p=="e" or p=="g":
            if q%2==0:
                return True
            else:
                return False
        if p=="b" or p=="d" or p=="f" or p=="h":
            if q%2==0:
                return False
            else:
                return True
            

        
