class Solution(object):
    def haveConflict(self, event1, event2):
        event1=[int(event1[0].replace(":","")),int(event1[1].replace(":",""))]
        event2=[int(event2[0].replace(":","")),int(event2[1].replace(":",""))]
        for x in range(event1[0],event1[1]+1):
            if x >= event2[0] and x <= event2[1]:
                return True
        return False
        
        
