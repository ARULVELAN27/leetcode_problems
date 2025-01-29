class Solution(object):
    def maximumValue(self, strs):
        max=0
        for x in strs:
            if x.isnumeric()==True :
                l=int(x)
                if l>max:
                    max=l
            elif x.isalpha()==True or x.isalnum()==True:
                l=len(x)
                if l>max:
                    max=l
            
        return max
        
