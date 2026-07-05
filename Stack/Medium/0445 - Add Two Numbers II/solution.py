# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prev=None
        cur=l1
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            
        prev2=None
        cur1=l2
        while cur1:
            nxt=cur1.next
            cur1.next=prev2
            prev2=cur1
            cur1=nxt
        

        dummy=ListNode(0)
        temp=dummy
        carry=0 
        l1=prev
        l2=prev2
        while l1 or l2 or carry:
            a=(l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            
            carry=a//10
            a=a%10
            temp.next=ListNode(a)
            temp=temp.next
            if l1:l1=l1.next 
            if l2:l2=l2.next
        
        prev2=None
        cur1=dummy.next
        while cur1:
            nxt=cur1.next
            cur1.next=prev2
            prev2=cur1
            cur1=nxt
        return prev2
