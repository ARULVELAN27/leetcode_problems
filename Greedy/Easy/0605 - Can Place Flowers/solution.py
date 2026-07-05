class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        a=0
        if len(flowerbed)>2:
            if flowerbed[0]==0 and flowerbed[1]==0:
                a=a+1
                flowerbed[0]=1
        if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
            a=a+1
            flowerbed[len(flowerbed)-1]=1
        for x in range(0,len(flowerbed)-2):
            if flowerbed[x]==0 and flowerbed[x-1]==0 and flowerbed[x+1]==0:
                a=a+1
                flowerbed[x]=1    
        if a>=n:
            return True
        return False


