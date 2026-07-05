class Solution(object):
    def sortTheStudents(self, s, k):
        s.sort(reverse=True,key=lambda x:x[k])
        return s
