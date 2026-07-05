class Solution(object):
    def average(self, salary):
        salary.sort()
        a=0
        for x in range(1,len(salary)-1):
            a=float(a+salary[x])
        return a/(len(salary)-2)
