class Solution(object):
    def canBeEqual(self, target, arr):
        for x in target:
            if arr.count(x)!=target.count(x):
                return False
        return True
