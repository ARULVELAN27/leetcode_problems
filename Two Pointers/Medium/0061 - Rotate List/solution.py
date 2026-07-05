# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        l=0
        temp=head
        while temp.next:
            l+=1
            temp=temp.next
        l+=1
        temp.next=head
        if k>l:
            k=k%l
        l=l-k
        for x in range(l):
            temp=temp.next
        head=temp.next
        temp.next=None
        return head
        
