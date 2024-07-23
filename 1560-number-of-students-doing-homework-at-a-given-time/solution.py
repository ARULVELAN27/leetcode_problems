class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        a=0
        for x in range(0,len(startTime)):
            for y in range(startTime[x],endTime[x]+1):
                if y==queryTime:
                    a=a+1
        return a 

    
        
