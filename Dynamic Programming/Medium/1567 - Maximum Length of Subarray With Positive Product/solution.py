class Solution(object):
    def maxVowels(self, s, k):
        count=0
        best=0
        l=0
        vovel="aeiou"
        for x in range(len(s)):
            if s[x] in vovel:
                count+=1
            while x-l+1>k:
                if s[l] in vovel:
                    count-=1
                l+=1
            best=max(best,count)
        return best


        
