class Solution(object):
    def tictactoe(self, moves):
        p=["z"]*9
        for x in moves:

            if moves.index(x)%2==0:
                p[(x[0]*3)+x[1]]="A"
            else:
                p[(x[0]*3)+x[1]]="B"
            if p[0]==p[1]==p[2]=="A" or p[3]==p[4]==p[5]=="A" or p[6]==p[7]==p[8]=="A" or p[0]==p[3]==p[6]=="A" or p[1]==p[4]==p[7]=="A" or p[2]==p[5]==p[8]=="A" or p[0]==p[4]==p[8]=="A" or p[2]==p[4]==p[6]=="A" :
                return "A"
            elif p[0]==p[1]==p[2]=="B" or p[3]==p[4]==p[5]=="B" or p[6]==p[7]==p[8]=="B" or p[0]==p[3]==p[6]=="B" or p[1]==p[4]==p[7]=="B" or p[2]==p[5]==p[8]=="B" or p[0]==p[4]==p[8]=="B" or p[2]==p[4]==p[6]=="B" :
                return "B"
        j="".join(p)
        print(j)
        if "A" in j:
            j=j.replace("A","")
        if "B" in j:
            j=j.replace("B","")
        print(j)
        if len(j)==0:
            return "Draw"
        
        return "Pending"
