class Solution(object):
    def numberOfSubstrings(self, s):
        d={}
        l=0
        count=0
        for x in range(len(s)):
            d[s[x]]=d.get(s[x],0)+1
            while len(d)==3:
                count+=len(s)-x
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
        return count
        
