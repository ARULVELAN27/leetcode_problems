class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        l=[]
        for x in strs:
            d["".join(sorted(x))]=d.get("".join(sorted(x)),[])+[x]
        for p in d.values():
            l.append(p)
        return l
        
