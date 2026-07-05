class Solution(object):
    def removeSubfolders(self, f):
        f.sort()
        l=[f[0]]
        for x in range(1,len(f)):
            if not f[x].startswith(l[-1]+"/"):
                l.append(f[x])
        return l

