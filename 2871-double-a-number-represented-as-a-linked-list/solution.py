# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        prev=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        dummy=ListNode(0)
        temp=dummy
        carry=0
        while prev or carry:
            a=(prev.val if prev else 0 )* 2+carry
            
            carry=a//10
            a=a%10

            temp.next=ListNode(a)
            if prev:prev=prev.next
            temp=temp.next


        dummy=dummy.next
        prev=None
        cur=dummy
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        return prev
            



        
