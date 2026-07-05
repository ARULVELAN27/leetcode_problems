class Solution(object):
    def judgeCircle(self, moves):
        a=[0,0]
        b=[0,0]
        for x in moves:
            if x=="R":
                a[0]=a[0]+1
            elif x=="L":
                a[0]=a[0]-1
            elif x=="U":
                a[1]=a[1]+1
            else:
                a[1]=a[1]-1
        if a==b:
            return True
        return False
        
