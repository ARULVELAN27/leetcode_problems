class Solution(object):
    def clearDigits(self, s):
        a=[]
        for x in s:
            if x.isnumeric()==True:
                a.pop()
            else:
                a.append(x)
        return "".join(a)


        
