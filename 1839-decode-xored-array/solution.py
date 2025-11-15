class Solution(object):
    def decode(self, e, pres):
        pres=[pres]
        for x in e:
            pres.append(pres[-1]^x)
        return pres
