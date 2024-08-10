class Solution(object):
    def checkIfPangram(self, sentence):
        a=['o', 'g', 'h', 'p', 'd', 'v', 'i', 'u', 'k', 'm', 'e', 'l', 'w', 'q', 'j', 's', 'r', 'y', 'c', 'x', 'a', 'z', 'n','f', 'b', 't']
        if len(a)==len(list(set(sentence))):
            return True
        
