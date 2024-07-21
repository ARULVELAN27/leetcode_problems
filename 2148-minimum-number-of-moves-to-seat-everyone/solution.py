class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        a=0
        for x in range(0,len(seats)):
            a=a+abs(seats[x]-students[x])
        return a
