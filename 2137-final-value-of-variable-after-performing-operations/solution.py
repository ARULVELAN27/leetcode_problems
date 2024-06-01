class Solution(object):
    def finalValueAfterOperations(self, operations):
        a=0
        for x in operations:
            if x=="--X" or x=="X--":
                a=a-1
            else:
                a=a+1
        return a
