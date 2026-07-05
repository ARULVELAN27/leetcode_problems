class Solution(object):
    def minimumPushes(self, word):
        p = {}
        for i in word:
            p[i] = p.get(i, 0) + 1

        o = "".join(sorted(word, key=lambda x: (-p[x], x)))

        a = ""
        for x in o:
            if x not in a:
                a = a + x

        cost = 0
        b = 1
        count = 0
        for x in a:
            if count >0 and count%8==0:
                b = b + 1
            cost = cost + (b * p[x])
            count = count + 1

        return cost

        
