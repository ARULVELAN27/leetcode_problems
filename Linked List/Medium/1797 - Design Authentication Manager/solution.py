class Solution(object):
    def interpret(self, command):
        a="()"
        b="(al)"
        s1 = command.replace(a, "o")
        d=s1.replace(b,"al")
        return d
        
