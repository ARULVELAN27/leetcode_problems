# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        a=[]
        while head:
            a.append(head.val)
            head=head.next

        a[k-1],a[-k]=a[-k],a[k-1]
        fake=ListNode(-1)
        temp=fake
        for x in a:
            temp.next=ListNode(x)
            temp=temp.next
        return fake.next
