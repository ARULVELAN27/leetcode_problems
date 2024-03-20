class Solution(object):
    def sortPeople(self, names, heights):
        l=[]
        l1=[]
        for y in heights:
            l.append(y)
        heights.sort(reverse=True)
        for x in range(0,len(heights)):
            for i in range(0,len(heights)):
                if heights[x]==l[i]:
                    l1.append(names[i])
        return l1
