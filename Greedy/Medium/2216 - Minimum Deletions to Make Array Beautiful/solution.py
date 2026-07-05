# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        t=head
        a=0
        while t:
            t=t.next
            a+=1
        a=a//2
        b=0
        dummy=ListNode(0)
        dummy.next=head
        l=dummy
        temp=dummy.next
        while temp:
            if b==a:
                l.next=temp.next
                return dummy.next
            b+=1
            l=l.next
            temp=temp.next

        
