# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if head==None or head.next==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        temp=dummy
        temp2=dummy
        a=0
        while a<left:
            a+=1
            temp2=temp
            temp=temp.next
        while a<=right:
            a+=1
            temp=temp.next
        prev=None
        curr=temp2.next
        for x in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        temp2.next=prev
        while temp2.next:
            temp2=temp2.next
        temp2.next=temp
        return dummy.next


        
