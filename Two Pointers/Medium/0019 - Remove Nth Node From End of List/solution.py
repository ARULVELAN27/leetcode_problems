# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        t=head
        a=0
        while t:
            a+=1
            t=t.next
        dummy=ListNode(0)
        dummy.next=head
        temp=dummy.next
        g=dummy
        a=a-n
        print(a)
        b=0
        while temp:
            if b==a:
                dummy.next=temp.next
                print(dummy.next,temp.next)
                break
            b=b+1
            dummy=dummy.next
            temp=temp.next
        return g.next

            



        
