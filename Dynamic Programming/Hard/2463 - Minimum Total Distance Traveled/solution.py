class Solution(object):
    def minimumRecolors(self, blocks, k):
        index=0
        max1=len(blocks)
        count=0
        white=0
        for x in blocks:
            if x=="W":
                white+=1
            count+=1
            if count==k:
                max1=min(max1,white)
                if blocks[index]=="W":
                    white-=1
                index+=1
                count-=1
        return max1

        
