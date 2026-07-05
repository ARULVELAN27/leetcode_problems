class Solution(object):
    def toHex(self, num):
        num1=num&0xFFFFFFFF
        f=""
        if num==0:
            return "0"
        hexa="0123456789abcdef"
        while num1>0:
            bit=num1%16
            f=hexa[bit]+f
            num1//=16
        return f
