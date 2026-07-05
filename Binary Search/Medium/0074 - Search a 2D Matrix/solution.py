class Solution(object):
    def searchMatrix(self, matrix, target):
        for x in matrix:
            if target in x:
                return True
        return False
