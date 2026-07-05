class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        best=0
        while l<r:
            best=max(best,(r-l)*(min(height[l],height[r])))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return best
        
