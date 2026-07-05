class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        a=0
        for x in hours:
            if x>=target:
                a=a+1
        return a
        
