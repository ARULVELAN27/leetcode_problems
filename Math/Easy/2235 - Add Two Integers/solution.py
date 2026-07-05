class Solution(object):
    def capitalizeTitle(self, title):
        a = ""
        title.lower()
        p = title.split()
        for x in range(len(p)):
            if len(p[x])>2:
                a = a + p[x].capitalize()
            else:
                a=a+p[x].lower()
            if x!=len(p)-1:
                a=a+" "
        return a

        
