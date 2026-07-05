class Solution(object):
    def kthCharacter(self, k):
        e="a"
        t=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while(len(e)<k):
            p=""
            for x in e:
                p=p+(t[((ord(x)-97)%26)+1])
            e=e+p
        return e[k-1]

        
