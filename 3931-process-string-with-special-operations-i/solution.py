class Solution(object):
    def processStr(self, s):
        a=[]
        for x in s:
            if x=="*":
                if len(a)>0:
                    a.pop()
            elif x=="#":
                a=a+a
            elif x=="%":
                a=a[::-1]
            else:
                a.append(x)
        return "".join(a)
        
