class Solution(object):
    def fizzBuzz(self, n):
        l=[]
        for x in range(0,n):
            a=x+1
            b=str(a)
            if a%3==0 and a%5==0:
                l.append("FizzBuzz")
            elif a%3==0:
                l.append("Fizz")
            elif a%5==0:
                l.append("Buzz")
            else:l.append(b)
        return l

             
        
