class Solution(object):
    def isSameAfterReversals(self, num):
        if num>=0:
            if num==0:
                return True
            for x in range(0,len(str(num))):
                if num%10==0:
                    return False
                else:
                    return True
        else:
            return False
        
