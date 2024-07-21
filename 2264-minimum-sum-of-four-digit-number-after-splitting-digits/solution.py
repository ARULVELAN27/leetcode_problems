class Solution(object):
    def minimumSum(self, num):
        l=[]
        for x in range(0,len(str(num))):
            l.append(num%10)
            num=int(num/10)
        l.sort()
        l.insert(1,l[3])
        l.pop(4)
        return ((int(l[0])*10+int(l[1]))+(int(l[2])*10+int(l[3])))
            
        
