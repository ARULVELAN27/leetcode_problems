class Solution(object):
    def finalString(self, s):
        z=[]
        j=''
        for x in range(0,len(s)):
            if s[x]=="i":
                z.reverse()
            else:
                z.append(s[x])
        return ((j.join(z)))

        
