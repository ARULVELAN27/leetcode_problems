# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, e):
        dummy=ListNode(0)
        dummy.next=head
        temp1=dummy
        temp2=dummy.next
        
        while temp2 :
            
            if temp2.val==e:
                temp1.next=temp2.next
                temp2=temp1.next
            else:
                temp1=temp2
                temp2=temp2.next

        return dummy.next            
        
