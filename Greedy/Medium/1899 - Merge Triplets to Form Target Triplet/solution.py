class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        a=0
        b=0
        if ruleKey=="type":
            b=0
        elif ruleKey=="color":
            b=1
        else:
            b=2
        for x in items:
            if x[b]==ruleValue:
                a=a+1
        return a
        
