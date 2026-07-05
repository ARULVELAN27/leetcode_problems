class Solution(object):
    def plusOne(self, digits):
        a=len(digits)
        if a>=2:

            e = int("".join(map(str, digits)))
            e=e+1
            o=[]
            o.append(e)
            output = list(map(int, str(o[0])))
            return output

    
        #     a=a-1
        #     k=digits[a]
        #     k=k+1
        #     digits[a]=k
        #     return digits
        else:
            w=digits[0]
            w=w+1
            l=[]
            l.append(w)
            output = list(map(int, str(l[0])))
            return output

        
        
      
       

  
        
