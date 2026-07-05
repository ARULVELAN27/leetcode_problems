# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, head1, head2):
        temp1=head1
        temp2=head2
        while temp1!=temp2:
            temp1=temp1.next if temp1 else head2
            temp2=temp2.next if temp2 else head1
        if temp1:
            return temp1
        return None
            
        
