class Solution(object):
    def defangIPaddr(self, address):
        x=address.replace(".","[.]")
        return x
