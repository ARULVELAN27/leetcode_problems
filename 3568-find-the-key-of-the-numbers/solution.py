class Solution(object):
    def generateKey(self, num1, num2, num3):
        b=""
        num1="0000"+str(num1)
        num2="0000"+str(num2)
        num3="0000"+str(num3)
        num1=num1[len(num1)-4:len(num1)]
        num2=num2[len(num2)-4:len(num2)]
        num3=num3[len(num3)-4:len(num3)]
        for x in range(4):
            b=b+min(num1[x],num2[x],num3[x])
        return int(b)
        
        
