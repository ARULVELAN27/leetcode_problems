class Solution(object):
    def similarPairs(self, words):
        l = []
        b = 1
        for x in words:
            for y in words[words.index(x) + 1:len(words)]:
                a = list(set(x))
                a.sort()
                a = "".join(a)
                b = list(set(y))
                b.sort()
                b = "".join(b)
                if a == b :
                    l.append(x)
                    l.append(y)
        if len(set(words))==1:
            return int(len(l) / 4)
        return int(len(l) / 2)

        
