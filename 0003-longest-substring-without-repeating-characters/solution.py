class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d={}
        l=0
        best=0
        for x in range(len(s)):
            d[s[x]]=d.get(s[x],0)+1
            while d[s[x]]>1:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            best=max(best,x-l+1) 
        return best
        
