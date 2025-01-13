class Solution(object):
    def findRelativeRanks(self, score):
        d=score[:]
        d.sort(reverse=True)
        ans=[]
        for x in score:
            e=str(d.index(x)+1)
            if e=="1":
                ans.append("Gold Medal")
            elif e=="2":
                ans.append("Silver Medal")
            elif e=="3":
                ans.append("Bronze Medal")
            else:
                ans.append(e)
        return ans

        
