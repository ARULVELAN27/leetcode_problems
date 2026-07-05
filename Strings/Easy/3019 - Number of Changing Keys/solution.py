class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        a=moves
        moves=moves.replace("_","R")
        a=a.replace("_","L")
        if abs(moves.count("L")-moves.count("R"))>abs(a.count("L")-a.count("R")):
            return abs(moves.count("L")-moves.count("R"))
        else:
            return abs(a.count("L")-a.count("R"))
        
        
