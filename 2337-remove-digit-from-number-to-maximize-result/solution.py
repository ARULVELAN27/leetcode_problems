class Solution(object):
    def removeDigit(self, number, digit):
        b = 0
        for x in range(len(number)):
            if number[x] == digit and int(number[0:x ] + number[x + 1:len(number)]) > b:
                b= int(number[0:x ] + number[x + 1:len(number)])
        return str(b)
        
