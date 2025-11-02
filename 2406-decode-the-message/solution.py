class Solution(object):
    def decodeMessage(self, k, m1):
        a="abcdefghijklmnopqrstuvwxyz"
        l=a[:]
        k=k.replace(" ","")
        key=""
        m=""
        for x in k:
            if x  in a:
                key=key+x
                a=a.replace(x,"")
        for x in m1:
            if x==" ":
                m=m+" "
            else:
                m=m+l[key.index(x)]
        return m

        
