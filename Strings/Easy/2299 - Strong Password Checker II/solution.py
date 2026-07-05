# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        dummy=ListNode(0)
        temp1=dummy
        
        temp=head
        c=0
        a=0
        while temp:
            if temp.val==0:
                c+=1
            if c==2:
                c-=1
                
                temp1.next=ListNode(a)
                temp1=temp1.next
                a=0
            a=a+temp.val
            temp=temp.next
        return dummy.next


        
