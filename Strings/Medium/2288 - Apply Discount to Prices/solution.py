class Solution(object):
    def countOperations(self, num1, num2):
        a=0
        while(num1>0 and num2>0):
            if num1>=num2:
                num1=num1-num2
                a=a+1
                
            elif num2>=num1:
                num2=num2-num1
                a=a+1
        return a

        
        
