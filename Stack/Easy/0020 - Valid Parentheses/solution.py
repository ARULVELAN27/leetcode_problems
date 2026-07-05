class Solution(object):
    def isValid(self, s):
        l=[]
        for x in s:
            if len(l)==0:
                l.append(x)
            else:
                if x==")":
                    if l[len(l)-1]=="(":
                        l.pop()
                    else:
                        return False
                elif x=="}":
                    if l[len(l)-1]=="{":
                        l.pop()
                    else:
                        return False
                elif x=="]":
                    if l[len(l)-1]=="[":
                        l.pop()
                    else:
                        return False
                else:
                    l.append(x)
        if len(l)==0:
            return True
        return False
                



        
