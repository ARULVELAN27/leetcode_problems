class Solution(object):
    def restoreString(self, s, indices):
        r=""
        for i in range(len(s)):
            r=r+s[indices.index(i)]
        return r

