class Solution(object):
    def findArray(self, pref):
        l=[]
        for x in range(len(pref)):
            if l==[]:
                l.append(pref[x])
            else:
                l.append(pref[x-1]^pref[x])
        return l
