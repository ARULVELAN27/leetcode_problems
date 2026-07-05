class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        a=""
        
        for x in range(min(len(s1),len(s2),len(s3))):
            if s1[x]==s2[x] and s2[x]==s3[x]:
                a=a+s1[x]
            else:
                break
        
        o=len(s1)-len(a)+len(s2)-len(a)+len(s3)-len(a)
        if len(a)==0:
            return -1
        return o

            
    

        
