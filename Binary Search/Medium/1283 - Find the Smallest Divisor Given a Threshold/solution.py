class Solution(object):
    def reformatDate(self, d):     
        p=""

        a=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d=d.split(" ")
        d=d[::-1]
        b=d[2]
        p=d[0]+"-"+("0"+str(a.index(d[1])+1) if len(str(a.index(d[1])+1))==1 else str(a.index(d[1])+1 ))+"-"+((b[0:len(b)-2] if len(b[0:len(b)-2])==2 else "0"+b[0:len(b)-2]))
        return p




