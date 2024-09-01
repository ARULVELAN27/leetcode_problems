class Solution(object):
    def countSeniors(self, details):
        a=0
        for x in details:
            b=int(x[11])*10+int(x[12])
            if b>60:
                a=a+1
        return a

        

